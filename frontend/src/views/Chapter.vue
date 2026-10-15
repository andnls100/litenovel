<script setup>
import { ref, onMounted, watch } from "vue"
import { useRoute, useRouter } from "vue-router"
import axios from "axios"

const route = useRoute()
const router = useRouter()

const bookInfo = ref({
    id: "",
    name: "",
    total: 0,
    chapters: []
})

const loading = ref(true)

async function loadChapters() {
    loading.value = true
    try {
        const res = await axios.get(
            `http://127.0.0.1:8000/api/chapters/${route.params.book}`
        )
        bookInfo.value = res.data
    } catch (err) {
        console.error(err)
        alert("加载章节失败")
    } finally {
        loading.value = false
    }
}

function goRead(chapter) {
    router.push(`/read/${bookInfo.value.id}/${chapter}/1`)
}

function goHome() {
    router.push("/")
}

onMounted(loadChapters)
watch(() => route.params.book, loadChapters)
</script>

<template>
    <div class="chapter-page">
        <!-- 顶部 -->
        <div class="header">
            <a href="javascript:;" class="back" @click="goHome">
                ← 返回首页
            </a>
            <h1>{{ bookInfo.name || "加载中..." }}</h1>
            <div class="total" v-if="!loading">
                共 {{ bookInfo.total }} 章
            </div>
        </div>

        <!-- 加载中 -->
        <div v-if="loading" class="loading">
            <div class="spinner"></div>
            <p>正在加载章节目录...</p>
        </div>

        <!-- 章节列表 -->
        <div v-else class="chapter-list">
            <div
                v-for="item in bookInfo.chapters"
                :key="item.chapter"
                class="chapter-item"
                @click="goRead(item.chapter)"
            >
                <div class="chapter-num">
                    {{ item.chapter }}
                </div>
                <div class="chapter-title">
                    {{ item.title }}
                </div>
                <div class="arrow">›</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.chapter-page {
    max-width: 860px;
    margin: 0 auto;
    padding: 40px 20px 60px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* 顶部 */
.header {
    text-align: center;
    margin-bottom: 36px;
}

.back {
    display: inline-block;
    color: #66b3ff;
    text-decoration: none;
    font-size: 14px;
    margin-bottom: 16px;
    transition: color 0.2s;
}

.back:hover {
    color: #3399ff;
    text-decoration: underline;
}

.header h1 {
    font-size: 28px;
    font-weight: 700;
    color: #1a1a1a;
    margin: 0 0 8px;
    line-height: 1.3;
}

.total {
    font-size: 14px;
    color: #888;
}

/* 加载中 */
.loading {
    text-align: center;
    padding: 80px 0;
    color: #999;
}

.spinner {
    width: 36px;
    height: 36px;
    border: 3px solid #e8e8e8;
    border-top-color: #66b3ff;
    border-radius: 50%;
    margin: 0 auto 16px;
    animation: spin 0.8s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

.loading p {
    margin: 0;
    font-size: 14px;
}

/* 章节列表 */
.chapter-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.chapter-item {
    display: flex;
    align-items: center;
    background: #ffffff;
    border-radius: 12px;
    padding: 14px 18px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    cursor: pointer;
    transition: all 0.2s ease;
    border: 1px solid transparent;
}

.chapter-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
    border-color: #e8f0fe;
    background: #fafcff;
}

/* 章节序号 */
.chapter-num {
    width: 36px;
    height: 36px;
    border-radius: 8px;
    background: #f0f5ff;
    color: #66b3ff;
    font-size: 14px;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-right: 14px;
}

.chapter-item:hover .chapter-num {
    background: #66b3ff;
    color: white;
}

/* 章节标题 */
.chapter-title {
    flex: 1;
    font-size: 15px;
    color: #333;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    padding-right: 12px;
}

/* 箭头 */
.arrow {
    font-size: 20px;
    color: #ccc;
    flex-shrink: 0;
    transition: all 0.2s;
}

.chapter-item:hover .arrow {
    color: #66b3ff;
    transform: translateX(3px);
}

/* 手机适配 */
@media (max-width: 600px) {
    .chapter-page {
        padding: 24px 14px 40px;
    }

    .header h1 {
        font-size: 22px;
    }

    .chapter-item {
        padding: 12px 14px;
    }

    .chapter-num {
        width: 32px;
        height: 32px;
        font-size: 13px;
        margin-right: 12px;
    }

    .chapter-title {
        font-size: 14px;
    }
}
</style>