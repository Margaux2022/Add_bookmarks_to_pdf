import re

'''
从自定义txt读取目录，txt格式：
[level title page]中间用空格分隔，title可以有空格.
level: 首位int
page: 末位int
txt示例：
1 Perspectives from a Comprehensive Evaluation of Reconstruction-based Anomaly Detection in Industrial Control Systems 1
2 1 Introduction 1
2 2 Background and Related Work 3
3 2.1 Industrial Control Systems: Threats and Defenses 3
3 2.2 ML Model Architectures for ICS Anomaly Detection 5

'''
def parse_titles_from_txt(txt_path):
    parsed_titles = []
    with open(txt_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去掉行末的换行符和多余空格
            line = line.strip()
            if line:
                # 按空格分隔行中的内容
                parts = line.split()
                level = int(parts[0])  # 第一个数字是层级
                page = int(parts[-1])   # 最后一个数字是页码
                title = ' '.join(parts[1:-1])  # 中间的内容是标题
                parsed_titles.append([level, title, page])

    return parsed_titles

# 指定你修改好的txt文件路径
txt_path = 'extracted_titles.txt'
titles = parse_titles_from_txt(txt_path)

print(f"Titles have been updated from {txt_path}")