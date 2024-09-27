import os
import re

def process_markdown_files(directory):
    # 处理普通的 Markdown 文件
    for filename in os.listdir(directory):
        if filename.endswith('.md') and filename != 'SUMMARY.md':
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            if lines:
                # 处理第一行，移除数字前缀并确保 # 后有一个空格
                lines[0] = re.sub(r'^# *\d+[-|｜]?', '# ', lines[0])
                # 如果 # 后没有空格，添加一个
                if lines[0].startswith('#') and not lines[0].startswith('# '):
                    lines[0] = '# ' + lines[0][1:].lstrip()
                # 在第一行后添加空白行
                lines.insert(1, '\n')

            # 更新文件名（去掉数字和分隔符）
            new_filename = re.sub(r'^\d+[-|｜]?', '', filename)
            new_filepath = os.path.join(directory, new_filename)

            # 写入修改后的内容
            with open(new_filepath, 'w', encoding='utf-8') as file:
                file.writelines(lines)

            # 如果文件名发生了变化，删除旧文件
            if new_filepath != filepath:
                os.remove(filepath)

    # 处理 SUMMARY.md 文件
    summary_path = os.path.join(directory, 'SUMMARY.md')
    if os.path.exists(summary_path):
        with open(summary_path, 'r', encoding='utf-8') as file:
            summary_content = file.read()

        # 更新 SUMMARY.md 中的链接
        summary_content = re.sub(r'\(./\d+[-|｜]?(.*?).md\)', r'(./\1.md)', summary_content)

        # 写入修改后的 SUMMARY.md
        with open(summary_path, 'w', encoding='utf-8') as file:
            file.write(summary_content)

    print("处理完成！")

# 执行脚本
if __name__ == "__main__":
    current_directory = os.getcwd()
    process_markdown_files(current_directory)
