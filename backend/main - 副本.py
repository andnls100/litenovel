from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import os
import json


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
# H:\novel-site\backend\books
# =========================

BASE_DIR = os.path.dirname(__file__)

BOOK_DIR = os.path.join(
    BASE_DIR,
    "books"
)


print("小说目录:", BOOK_DIR)



# =========================
# 读取小说映射
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
# 根据ID获取小说
# =========================

def get_book(book_id):

    books = load_books()


    for book in books:

        if book["id"] == book_id:

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


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


HOT_FILE = os.path.join(
    BOOK_DIR,
    "hot.txt"
)


@app.get("/api/hot")
def hot_books():

    books = load_books()

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


    result = []


    for book_id in ids:

        for book in books:

            if book["id"] == book_id:

                result.append(book)

                break


    return result
# =========================
# 读取txt
# =========================

def load_txt(book):

    path = os.path.join(
        BOOK_DIR,
        book["file"] + ".txt"
    )


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()



# =========================
# 测试
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



# =========================
# 阅读接口
#
# /api/read/001/1/1
#
# book_id / chapter / page
# =========================

@app.get(
    "/api/read/{book_id}/{chapter}/{page}"
)
def read(
    book_id: str,
    chapter: int,
    page: int
):


    # 获取小说

    book = get_book(book_id)


    if not book:

        raise HTTPException(
            404,
            "小说不存在"
        )



    # 获取索引

    index = load_index(book)


    chapters = index["chapters"]



    # 找章节

    current = None


    for c in chapters:


        if c["id"] == chapter:

            current = c

            break



    if current is None:

        raise HTTPException(
            404,
            "章节不存在"
        )



    # 当前章节分页

    pages = current["pages"]



    if page < 1 or page > len(pages):

        raise HTTPException(
            404,
            "页码不存在"
        )



    # 读取正文

    text = load_txt(book)



    # 当前页范围

    p = pages[page-1]


    content = text[
        p["start"]:
        p["end"]
    ]



    return {


        # 小说ID

        "id": book["id"],



        # 小说名称

        "book": book["name"],



        # 章节

        "chapter": chapter,



        # 标题

        "title": current["title"],



        # 当前页

        "page": page,



        # 总页数

        "total_page": len(pages),



        # 正文

        "content": content,



        # 上一页

        "prev_page":
            page-1
            if page > 1
            else None,



        # 下一页

        "next_page":
            page+1
            if page < len(pages)
            else None,



        # 上一章

        "prev_chapter":
            chapter-1
            if chapter > 1
            else None,



        # 下一章

        "next_chapter":
            chapter+1
            if chapter < len(chapters)
            else None

    }