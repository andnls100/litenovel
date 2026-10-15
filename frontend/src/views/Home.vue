<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"

const books = ref([])
const router = useRouter()

async function load() {
    const res = await axios.get("http://127.0.0.1:8000/api/hot")
    books.value = res.data
}

function read(id) {
    router.push(`/read/${id}/1/1`)
}

onMounted(load)
</script>

<template>
    <div class="home">
        <!-- 顶部标题区 -->
        <header class="header">
            <div class="header-content">
                <h1>热门榜</h1>
                <p>今日最受欢迎的小说推荐</p>
            </div>
        </header>

        <!-- 小说列表 -->
        <div class="list">
            <div
                class="item"
                v-for="(book, index) in books"
                :key="book.id"
                @click="read(book.id)"
            >
                <!-- 排名 -->
                <div
                    class="rank"
                    :class="{
                        'rank-1': index === 0,
                        'rank-2': index === 1,
                        'rank-3': index === 2
                    }"
                >
                    {{ index + 1 }}
                </div>

                <!-- 封面 -->
                <div class="cover">
                    <img :src="'/images/' + book.id + '.jpg'" :alt="book.name" />
                </div>

                <!-- 信息 -->
                <div class="info">
                    <h2 class="title">{{ book.name }}</h2>
                    <p class="desc">{{ book.file }}</p>
                </div>

                <!-- 箭头 -->
                <div class="arrow">›</div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.home {
    max-width: 860px;
    margin: 0 auto;
    padding: 40px 20px 60px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* 顶部标题 */
.header {
    text-align: center;
    margin-bottom: 40px;
}

.header h1 {
    font-size: 36px;
    font-weight: 700;
    color: #1a1a1a;
    margin: 0 0 8px;
    letter-spacing: 1px;
}

.header p {
    font-size: 15px;
    color: #888;
    margin: 0;
}

/* 列表 */
.list {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

/* 每一项 */
.item {
    display: flex;
    align-items: center;
    background: #ffffff;
    border-radius: 14px;
    padding: 14px 18px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
    cursor: pointer;
    transition: all 0.22s ease;
    border: 1px solid transparent;
}

.item:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
    border-color: #e8f0fe;
}

/* 排名 */
.rank {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: #f0f0f0;
    color: #666;
    font-size: 15px;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-right: 16px;
}

/* 前三名特殊颜色 */
.rank-1 {
    background: linear-gradient(135deg, #ff6b35, #ff8c42);
    color: white;
    box-shadow: 0 2px 8px rgba(255, 107, 53, 0.35);
}

.rank-2 {
    background: linear-gradient(135deg, #ff9f43, #ffb142);
    color: white;
}

.rank-3 {
    background: linear-gradient(135deg, #54a0ff, #2e86de);
    color: white;
}

/* 封面 */
.cover {
    width: 64px;
    height: 86px;
    border-radius: 8px;
    overflow: hidden;
    flex-shrink: 0;
    margin-right: 16px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.cover img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.3s ease;
}

.item:hover .cover img {
    transform: scale(1.05);
}

/* 文字信息 */
.info {
    flex: 1;
    min-width: 0;
    padding-right: 12px;
}

.title {
    font-size: 17px;
    font-weight: 600;
    color: #222;
    margin: 0 0 6px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.desc {
    font-size: 13px;
    color: #999;
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* 右侧箭头 */
.arrow {
    font-size: 22px;
    color: #ccc;
    flex-shrink: 0;
    transition: all 0.2s;
}

.item:hover .arrow {
    color: #66b3ff;
    transform: translateX(3px);
}

/* 响应式 */
@media (max-width: 600px) {
    .home {
        padding: 24px 14px 40px;
    }

    .header h1 {
        font-size: 28px;
    }

    .item {
        padding: 12px 14px;
    }

    .rank {
        width: 28px;
        height: 28px;
        font-size: 14px;
        margin-right: 12px;
    }

    .cover {
        width: 56px;
        height: 76px;
        margin-right: 12px;
    }

    .title {
        font-size: 15px;
    }

    .desc {
        font-size: 12px;
    }
}
</style>