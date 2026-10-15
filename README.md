
# litenovel
A lightweight local novel reading website built with FastAPI and Vue 3. Supports TXT novels with automatic chapter indexing and pagination.

# Novel Site - 轻量级小说阅读网站

一个基于 **FastAPI + Vue3** 的本地小说阅读网站，支持 TXT 小说自动分章、分页阅读，界面简洁美观。

---

## 项目架构

```
novel-site/
├── backend/                     # 后端 (FastAPI)
│   ├── books/                   # 小说资源目录
│   │   ├── *.txt                # 小说原文
│   │   ├── *.idx                # 章节索引文件（自动生成）
│   │   └── books.json           # 小说ID与文件名映射（自动生成）
│   ├── make_idx.py              # 生成章节索引脚本
│   ├── generate_books.py        # 生成 books.json 脚本
│   ├── main.py                  # FastAPI 主入口
│   └── ...
│
└── frontend/                    # 前端 (Vue3)
    ├── src/
    │   ├── views/
    │   │   ├── Home.vue         # 热门榜首页
    │   │   ├── Chapter.vue      # 章节目录页
    │   │   └── Read.vue         # 阅读页
    │   ├── router/
    │   └── ...
    └── ...
```

### 技术栈

| 部分     | 技术                          |
|----------|-------------------------------|
| 后端     | FastAPI + Python              |
| 前端     | Vue 3 + Vue Router + Axios    |
| 数据存储 | 本地 TXT + JSON 索引          |
| 接口风格 | RESTful API                   |

### 核心功能

- 热门小说榜单
- 章节目录浏览
- 分页阅读（支持跨章节翻页）
- 上一章 / 下一章 / 上一页 / 下一页 完整导航
- 自动生成章节索引（`.idx`）
- 响应式界面（支持手机）

---

## 安装与使用

### 1. 环境要求

- Python 3.9+
- Node.js 18+
- npm 或 pnpm

### 2. 后端安装

```bash
cd backend

# 安装依赖
pip install fastapi uvicorn

# 如果有 requirements.txt
pip install -r requirements.txt
```

### 3. 准备小说文件

1. 把你的小说 TXT 文件放到：

```
backend/books/
```

文件名示例：

```
万界疯人院.txt
斗破苍穹.txt
遮天.txt
```

> **注意**：TXT 文件请使用 **UTF-8** 编码。

2. 生成小说列表（books.json）

```bash
cd backend
python generate_books.py
```

执行后会在 `books/` 目录下生成 `books.json`，格式如下：

```json
[
  {
    "id": "000000001",
    "name": "万界疯人院",
    "file": "万界疯人院"
  }
]
```

3. 生成章节索引（.idx 文件）

```bash
python make_idx.py
```

该脚本会为每本小说生成对应的 `.idx` 索引文件，包含章节标题和每页的起止位置。

### 4. 启动后端

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

启动成功后可访问接口文档：

- Swagger UI：http://127.0.0.1:8000/docs

### 5. 前端安装与启动

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

默认访问地址：http://localhost:5173

---

## 接口说明

| 方法 | 路径                                    | 说明                   |
|------|-----------------------------------------|------------------------|
| GET  | `/api/hot`                              | 获取热门小说列表       |
| GET  | `/api/books`                            | 获取全部小说列表       |
| GET  | `/api/chapters/{book_id}`               | 获取某本小说章节目录   |
| GET  | `/api/read/{book_id}/{chapter}/{page}`  | 获取指定章节的某一页内容 |

### 阅读接口返回示例

```json
{
  "id": "000000001",
  "book": "万界疯人院",
  "chapter": 1,
  "title": "第一章 万圣节",
  "page": 1,
  "total_page": 2,
  "content": "正文内容...",
  "prev_page": null,
  "next_page": 2,
  "prev_chapter": null,
  "prev_chapter_total_page": null,
  "next_chapter": 2
}
```

---

## 使用流程总结

1. 把 TXT 小说放入 `backend/books/`
2. 运行 `python generate_books.py` 生成 `books.json`
3. 运行 `python make_idx.py` 生成章节索引
4. 启动后端：`uvicorn main:app --reload --port 8000`
5. 启动前端：`npm run dev`
6. 浏览器打开前端地址即可开始阅读

---

## 目录结构建议

```
backend/books/
├── books.json
├── 万界疯人院.txt
├── 万界疯人院.idx
├── 斗破苍穹.txt
├── 斗破苍穹.idx
└── ...
```

---

## 注意事项

1. **编码问题**：TXT 文件必须是 UTF-8 编码，否则可能出现乱码。
2. **索引更新**：新增或替换小说后，需要重新运行 `generate_books.py` 和 `make_idx.py`。
3. **封面图片**（可选）：如需显示封面，请将图片放到前端的 `public/images/` 目录，命名为 `{book_id}.jpg`。
4. **跨域**：开发环境下前端默认请求 `http://127.0.0.1:8000`，如有跨域问题请在 FastAPI 中开启 CORS。

---

## License

MIT License
```
 
