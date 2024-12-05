# Add_bookmarks_to_pdf

从PDF文件中提取标题并为其添加书签，以改善文档的导航体验。
使用了`PyMuPDF`和`PyPDF2`库来完成这些任务。

## 功能

- 从指定的PDF文件中提取标题及其对应的页码。
- 支持以多级标题的形式提取样式（如 "1", "1.1", "1.1.1"）。
- 将提取的标题自动添加为书签, 方便跳转对应页面。

## 环境要求

确保您的环境中已经安装以下Python库：

- PyMuPDF
- PyPDF2

您可以通过以下命令安装所需的库：

''' 

pip install PyMuPDF PyPDF2

''' 

## 使用方法

将要处理的PDF文件放在脚本目录下，并命名为 1.pdf（可以根据需要修改脚本中的文件名）。
运行脚本：

''' 
python main.py
'''
 
脚本完成后，输出将生成一个新的PDF文件，书签会被添加到 pdf_with_bookmarks.pdf。

## 脚本工作原理
'extract_headings(pdf_path)': 该函数从PDF中提取以数字序号格式表示的标题及其对应的页码。
'parse_title_level(title)': 解析标题层级，根据标题中点的数量来判断层级。
'add_bookmarks_to_pdf(input_pdf_path, output_pdf_path, titles)': 向PDF文档中添加书签。
## 示例输出
在成功提取标题后，打印提取到的标题及其页码，例如：
```bash
Title: 1 Introduction, Page: 1
Title: 1.1 Background, Page: 3
...
Bookmarks have been added!
