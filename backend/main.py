from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import os
import json
import chardet


app = FastAPI()



# =========================
# 跨域
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# =========================
# 小说目录
# =========================

BASE_DIR = os.path.dirname(__file__)

BOOK_DIR = os.path.join(
    BASE_DIR,
    "books"
)


print("小说目录:", BOOK_DIR)



# =========================
# 自动读取文本
# =========================

def read_file(path):

    with open(path, "rb") as f:
        data = f.read()


    result = chardet.detect(data)

    encoding = result["encoding"] or "utf-8"


    try:
        return data.decode(encoding)

    except:

        return data.decode(
            "gb18030",
            errors="ignore"
        )



# =========================
# books.json
# =========================

def load_books():

    path = os.path.join(
        BOOK_DIR,
        "books.json"
    )


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



# =========================
# 根据ID找书
# =========================

def get_book(book_id):

    books = load_books()


    for book in books:


        if str(book["id"]) == str(book_id):

            return book


    return None



# =========================
# 读取idx
# =========================

def load_index(book):


    path = os.path.join(
        BOOK_DIR,
        book["file"] + ".idx"
    )


    if not os.path.exists(path):

        raise HTTPException(
            404,
            "索引不存在"
        )


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)




# =========================
# 热门
# =========================

HOT_FILE = os.path.join(
    BOOK_DIR,
    "hot.txt"
)


@app.get("/api/hot")
def hot_books():


    books = load_books()


    if not os.path.exists(HOT_FILE):

        return []



    with open(
        HOT_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        ids = [
            x.strip()
            for x in f.readlines()
            if x.strip()
        ]



    result=[]


    for book_id in ids:


        book=get_book(book_id)


        if book:

            result.append(book)



    return result




# =========================
# 首页
# =========================

@app.get("/")
def root():

    return {
        "msg":"小说服务器运行正常"
    }




# =========================
# 小说列表
# =========================

@app.get("/api/books")
def books():

    return load_books()


@app.get("/api/chapters/{book_id}")
def get_chapters(book_id: str):
    """获取某本小说的全部章节目录（从 .idx 文件读取）"""
    
    # 1. 读取 books.json 找到对应小说
    books_json_path = os.path.join(BOOK_DIR, "books.json")
    if not os.path.exists(books_json_path):
        raise HTTPException(status_code=500, detail="books.json 不存在")
    
    with open(books_json_path, "r", encoding="utf-8") as f:
        books = json.load(f)
    
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="小说不存在")
    
    # 2. 读取对应的 .idx 文件
    idx_path = os.path.join(BOOK_DIR, book["file"] + ".idx")
    if not os.path.exists(idx_path):
        raise HTTPException(status_code=404, detail="索引文件不存在")
    
    with open(idx_path, "r", encoding="utf-8") as f:
        idx_data = json.load(f)
    
    # 3. 从 idx 中提取章节列表
    chapters = []
    for i, ch in enumerate(idx_data.get("chapters", []), start=1):
        chapters.append({
            "chapter": i,                    # 章节序号（从1开始，给前端用）
            "id": ch.get("id"),              # 原始章节id（如 0001）
            "title": ch.get("title", ""),    # 章节标题
            "page_count": len(ch.get("pages", []))  # 这一章有多少页（可选）
        })
    
    return {
        "id": book["id"],
        "name": book["name"],
        "author": idx_data.get("author", ""),
        "total": len(chapters),
        "chapters": chapters
    }

# =========================
# 阅读接口
#
# /api/read/000000001/1/1
#
# =========================

@app.get("/api/read/{book_id}/{chapter}/{page}")
def read(
    book_id: str,
    chapter: int,
    page: int
):
    # 找小说
    book = get_book(book_id)
    if not book:
        raise HTTPException(404, "小说不存在")

    # 读取索引
    index = load_index(book)
    chapters = index.get("chapters", [])

    # 找当前章节
    current = None
    current_index = -1
    for i, c in enumerate(chapters):
        if int(c["id"]) == chapter:
            current = c
            current_index = i
            break

    if current is None:
        raise HTTPException(404, "章节不存在")

    pages = current["pages"]
    if page < 1 or page > len(pages):
        raise HTTPException(404, "页码不存在")

    # 读取正文
    txt_path = os.path.join(BOOK_DIR, book["file"] + ".txt")
    text = read_file(txt_path)
    p = pages[page - 1]
    content = text[p["start"]:p["end"]]

    # ========== 计算上一章 / 下一章信息 ==========
    prev_chapter = None
    prev_chapter_total_page = None
    next_chapter = None

    if current_index > 0:
        prev_chapter = int(chapters[current_index - 1]["id"])
        prev_chapter_total_page = len(chapters[current_index - 1]["pages"])

    if current_index < len(chapters) - 1:
        next_chapter = int(chapters[current_index + 1]["id"])

    return {
        "id": book["id"],
        "book": book["name"],
        "chapter": chapter,
        "title": current["title"],
        "page": page,
        "total_page": len(pages),
        "content": content,

        # 页码导航
        "prev_page": page - 1 if page > 1 else None,
        "next_page": page + 1 if page < len(pages) else None,

        # 章节导航
        "prev_chapter": prev_chapter,
        "prev_chapter_total_page": prev_chapter_total_page,  # 新增：上一章总页数
        "next_chapter": next_chapter
    }