<script setup>
import {
    ref,
    onMounted,
    watch
} from "vue"
import {
    useRoute,
    useRouter
} from "vue-router"
import axios from "axios"

const route = useRoute()
const router = useRouter()
const data = ref({})

async function load() {
    try {
        let res = await axios.get(
            "http://127.0.0.1:8000/api/read/" +
            route.params.book + "/" +
            route.params.chapter + "/" +
            route.params.page
        )
        data.value = res.data
    } catch (err) {
        console.error(err)
        alert("加载失败")
    }
}

// 返回目录
function goCatalog() {
    router.push(`/chapter/${data.value.id || route.params.book}`)
}

// 翻页（支持跨章）
function goPage(type) {
    // 下一页
    if (type === 'next') {
        if (data.value.next_page) {
            router.push(
                `/read/${data.value.id}/${data.value.chapter}/${data.value.next_page}`
            )
        } else if (data.value.next_chapter) {
            router.push(
                `/read/${data.value.id}/${data.value.next_chapter}/1`
            )
        } else {
            alert("下一页没有了")
        }
        return
    }

    // 上一页
    if (type === 'prev') {
        if (data.value.prev_page) {
            router.push(
                `/read/${data.value.id}/${data.value.chapter}/${data.value.prev_page}`
            )
        } else if (data.value.prev_chapter) {
            const lastPage = data.value.prev_chapter_total_page || 1
            router.push(
                `/read/${data.value.id}/${data.value.prev_chapter}/${lastPage}`
            )
        } else {
            alert("上一页没有了")
        }
        return
    }
}

// 章节跳转
function goChapter(type) {
    if (type === 'prev') {
        if (data.value.prev_chapter) {
            router.push(
                `/read/${data.value.id}/${data.value.prev_chapter}/1`
            )
        } else {
            alert("上一章没有了")
        }
    } else if (type === 'next') {
        if (data.value.next_chapter) {
            router.push(
                `/read/${data.value.id}/${data.value.next_chapter}/1`
            )
        } else {
            alert("下一章没有了")
        }
    }
}

onMounted(load)
watch(
    () => route.params,
    () => load()
)
</script>

<template>
    <div class="reader">
        <!-- 顶部信息 -->
        <div class="header">
            <div class="book-name">{{ data.book }}</div>
            <h1 class="chapter-title">{{ data.title }}</h1>
        </div>

        <!-- 顶部导航 -->
        <div class="nav">
            <a href="javascript:;" @click="goCatalog">目录</a>
            <a href="javascript:;" @click="goChapter('prev')">上一章</a>
            <a href="javascript:;" @click="goPage('prev')">上一页</a>
            <span class="page-info">
                第 {{ data.page }} / {{ data.total_page }} 页
            </span>
            <a href="javascript:;" @click="goPage('next')">下一页</a>
            <a href="javascript:;" @click="goChapter('next')">下一章</a>
        </div>

        <!-- 正文区域 -->
        <div class="content-box">
            <div class="content">
                {{ data.content }}
            </div>
        </div>

        <!-- 底部导航 -->
        <div class="nav">
            <a href="javascript:;" @click="goCatalog">目录</a>
            <a href="javascript:;" @click="goChapter('prev')">上一章</a>
            <a href="javascript:;" @click="goPage('prev')">上一页</a>
            <span class="page-info">
                第 {{ data.page }} / {{ data.total_page }} 页
            </span>
            <a href="javascript:;" @click="goPage('next')">下一页</a>
            <a href="javascript:;" @click="goChapter('next')">下一章</a>
        </div>
    </div>
</template>

<style scoped>
.reader {
    max-width: 860px;
    margin: 0 auto;
    padding: 40px 20px 60px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* 顶部信息 */
.header {
    text-align: center;
    margin-bottom: 28px;
}

.book-name {
    font-size: 14px;
    color: #888;
    margin-bottom: 10px;
    letter-spacing: 0.5px;
}

.chapter-title {
    font-size: 24px;
    font-weight: 700;
    color: #1a1a1a;
    margin: 0;
    line-height: 1.4;
}

/* 导航栏 */
.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #ffffff;
    border-radius: 12px;
    padding: 12px 20px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    margin: 16px 0;
    border: 1px solid #f0f0f0;
}

.nav a {
    color: #66b3ff;
    text-decoration: none;
    font-size: 14px;
    cursor: pointer;
    padding: 4px 6px;
    border-radius: 6px;
    transition: all 0.2s;
}

.nav a:hover {
    color: #3399ff;
    background: #f0f7ff;
}

.page-info {
    color: #666;
    font-size: 13px;
    background: #f5f7fa;
    padding: 4px 12px;
    border-radius: 20px;
}

/* 正文区域 */
.content-box {
    background: #ffffff;
    border-radius: 14px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.05);
    padding: 36px 40px;
    margin: 20px 0;
    border: 1px solid #f0f0f0;
}

.content {
    font-size: 18px;
    line-height: 1.9;
    color: #333;
    white-space: pre-wrap;
    word-break: break-word;
    letter-spacing: 0.3px;
}

/* 手机适配 */
@media (max-width: 600px) {
    .reader {
        padding: 24px 12px 40px;
    }

    .chapter-title {
        font-size: 20px;
    }

    .nav {
        padding: 10px 12px;
        flex-wrap: wrap;
        gap: 8px;
        justify-content: center;
    }

    .nav a {
        font-size: 13px;
    }

    .page-info {
        font-size: 12px;
        order: -1;
        width: 100%;
        text-align: center;
        margin-bottom: 4px;
    }

    .content-box {
        padding: 24px 18px;
        border-radius: 12px;
    }

    .content {
        font-size: 16px;
        line-height: 1.85;
    }
}
</style>