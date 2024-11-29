import fitz  # PyMuPDF
import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
import re

def extract_headings(pdf_path):
    """
    从指定PDF文件中提取标题及其对应页码。

    :param pdf_path: 要提取标题的PDF文件路径
    :return: 包含标题和页码的列表
    """
    doc = fitz.open(pdf_path)
    headings = []

    # 正则表达式匹配数字序号（例如 "1", "1.1", "1.1.1" 等）
    heading_pattern = re.compile(r'^\d+(\.\d+)*\s*$')

    # 提取每一页的文本块
    for page_num in range(len(doc)):
        page = doc[page_num]
        text_blocks = page.get_text("blocks")  # 获取页面中的文本块

        for block in text_blocks:
            text = block[4].strip()  # 获取文本内容并移除前后的空格
            lines = text.splitlines()

            # 处理包含标题的文本块
            if len(lines) == 2:
                first_line = lines[0].strip()  # 第一行，数字序号
                second_line = lines[1].strip()  # 第二行，标题内容

                # 判断第一行是否为标题格式
                if heading_pattern.match(first_line) and second_line and not re.search(r'[^\w\s]', second_line):
                    full_heading = f"{first_line} {second_line}"
                    headings.append((full_heading, page_num))

    return headings

def parse_title_level(title):
    """
    解析标题的层级。

    :param title: 字符串格式标题
    :return: 标题层级
    """
    return title.count('.') + 1  # 层级由点的数量决定

def add_bookmarks_to_pdf(input_pdf_path, output_pdf_path, titles):
    """
    向PDF文件添加书签。

    :param input_pdf_path: 输入PDF文件的路径
    :param output_pdf_path: 输出PDF文件的路径
    :param titles: 包含标题和页码的列表
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    # 添加页面到新PDF文档
    for page in reader.pages:
        writer.add_page(page)

    bookmarks = [None] * 4  # 假设最大层级为4
    for level, title, page_number in titles:
        parent = bookmarks[level - 1] if level > 1 else None  # 确定父书签
        bookmark = writer.add_outline_item(title, page_number, parent)
        bookmarks[level - 1] = bookmark  # 更新当前层级的书签

    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)

if __name__ == '__main__':
    pdf_path = "1.pdf"  # 要添加书签的PDF文件
    output_pdf_path = 'pdf_with_bookmarks.pdf'  # 输出PDF文件
    headings = extract_headings(pdf_path)

    # 获取标题和层级
    titles = [(parse_title_level(row[0]), row[0], row[1]) for row in headings]

    # 添加书签
    add_bookmarks_to_pdf(pdf_path, output_pdf_path, titles)

    # 打印提取的标题
    for title, page in headings:
        print(f"Title: {title}, Page: {page + 1}")

    print("Bookmarks have been added!")