import fitz  # PyMuPDF
from PyPDF2 import PdfReader, PdfWriter
import re

pdf_path = '2.pdf'
doc = fitz.open(pdf_path)
toc = doc.get_toc()
output_pdf_path = 'book_with_bookmarks.pdf' 

#输出toc到txt文件
output_file_path = 'extracted_titles.txt'
with open(output_file_path, 'w', encoding='utf-8') as f:
    for level, title, page in toc:
        # 在每个标题后面添加换行符
        f.write(f"{level} {title.strip()} {page}"+"\n")  

print(f"Titles have been written to {output_file_path}")
