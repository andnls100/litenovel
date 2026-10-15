import os
import json


BOOK_DIR = "books"

OUTPUT = "books/books.json"



def generate_books():


    books = []


    # 获取txt文件，跳过hot.txt

    files = [
        f for f in os.listdir(BOOK_DIR)
        if f.lower().endswith(".txt")
        and f.lower() != "hot.txt"
    ]


    # 排序，保证编号稳定

    files.sort()



    for index, file in enumerate(files, start=1):


        # 去掉扩展名

        name = os.path.splitext(file)[0]


        # 9位编号 000000001

        book_id = f"{index:09d}"



        books.append({

            "id": book_id,

            "name": name,

            "file": name

        })



    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            books,
            f,
            ensure_ascii=False,
            indent=4
        )


    print(
        f"生成完成，共 {len(books)} 本小说"
    )



if __name__ == "__main__":

    generate_books()