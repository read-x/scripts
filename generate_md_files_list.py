import os
import re

def generate_md_list():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 获取当前目录下所有的 .md 文件
    md_files = [f for f in os.listdir(current_dir) if f.endswith('.md')]
    
    # 定义正则表达式来匹配文件名开头的数字和分隔符
    pattern = re.compile(r'^(\d+[｜|])?(.*?)\.md$')
    
    # 解析文件名并排序
    parsed_files = []
    for file in md_files:
        match = pattern.match(file)
        if match:
            number = match.group(1) or ''  # 如果没有序号，使用空字符串
            name = match.group(2)
            parsed_files.append((number, name, file))
    
    # 按序号排序
    parsed_files.sort(key=lambda x: x[0])
    
    # 生成格式化的字符串列表
    formatted_list = []
    for _, name, file in parsed_files:
        formatted_line = f"- [{name}](./{file})"
        formatted_list.append(formatted_line)
    
    # 将列表写入文件
    with open('md_list.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(formatted_list))
    
    print("列表已生成并保存到 md_list.md 文件中。")

# 运行函数
generate_md_list()
