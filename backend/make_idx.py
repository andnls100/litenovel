import os
import re
import json
import chardet


BOOK_DIR = "books"

# 每页多少字符
PAGE_SIZE = 2000


# 章节匹配
CHAPTER_PATTERN = re.compile(
    r"^第[0-9零一二三四五六七八九十百千万]+章.*$",
    re.MULTILINE
)


def read_text(file):

    """
    自动识别小说编码
    支持 UTF-8 / GBK / GB18030
    """

    with open(file, "rb") as f:
        data = f.read()

    result = chardet.detect(data)

    encoding = result["encoding"]

    if not encoding:
        encoding = "utf-8"

    print(
        "编码:",
        encoding
    )

    try:
        return data.decode(encoding)

    except UnicodeDecodeError:

        # 兜底
        return data.decode(
            "gb18030",
            errors="ignore"
        )



def get_chapters(text):
    """
    获取章节位置
    """

    result = []

    matches = list(
        CHAPTER_PATTERN.finditer(text)
    )


    for i, m in enumerate(matches):

        start = m.start()

        title = m.group().strip()


        if i < len(matches)-1:

            end = matches[i+1].start()

        else:

            end = len(text)


        result.append({

            "title": title,

            "start": start,

            "end": end

        })


    return result



def make_pages(start,end):

    """
    根据章节范围分页
    """

    pages=[]

    pos=start


    page_id = 1


    while pos < end:

        page_end=min(
            pos+PAGE_SIZE,
            end
        )


        pages.append({

            # 000000001格式
            "id": str(page_id).zfill(4),

            "start": pos,

            "end": page_end

        })


        pos=page_end

        page_id += 1


    return pages




def build_index(txt_file):


    name=os.path.splitext(
        os.path.basename(txt_file)
    )[0]


    print(
        "处理:",
        name
    )


    text = read_text(txt_file)



    chapters=get_chapters(text)



    idx={

        "book":name,

        "author":"",

        "chapters":[]

    }



    for i,c in enumerate(chapters):


        item={

            # 章节ID 00001
            "id": str(i+1).zfill(4),

            "title":c["title"],

            "pages":make_pages(
                c["start"],
                c["end"]
            )

        }


        idx["chapters"].append(item)



    idx_file=txt_file.replace(
        ".txt",
        ".idx"
    )



    with open(
        idx_file,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(
            idx,
            f,
            ensure_ascii=False,
            indent=2
        )



    print(
        "生成:",
        idx_file,
        "章节:",
        len(chapters)
    )





def main():


    for file in os.listdir(BOOK_DIR):


        # 跳过 hot.txt
        if file.lower() == "hot.txt":
            continue


        if file.endswith(".txt"):


            path=os.path.join(
                BOOK_DIR,
                file
            )


            build_index(path)



if __name__=="__main__":

    main()