# Add_bookmarks_to_pdf

该项目旨在从PDF文件中提取标题并为其添加书签，以改善文档的导航体验。脚本使用了`PyMuPDF`和`PyPDF2`库来完成这些任务。

## 功能

- 从指定的PDF文件中提取标题及其对应的页码。
- 支持以多级标题的形式提取样式（如 "1", "1.1", "1.1.1"）。
- 将提取的标题自动添加为书签, 方便浏览。

## 环境要求

确保您的环境中已经安装以下Python库：

- PyMuPDF
- PyPDF2

您可以通过以下命令安装所需的库：

```bash
pip install PyMuPDF PyPDF2
