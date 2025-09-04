#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown 文档整理脚本
功能：
1. 按照 MD 文件名前的数字排序
2. 生成 SUMMARY.md，去掉文件名的数字前缀
3. 重命名 MD 文件，去掉数字前缀
4. 修改文件内容，去掉第一行的数字前缀
"""

import os
import re
import shutil
from pathlib import Path

def extract_number_from_filename(filename):
    """从文件名中提取数字前缀"""
    # 匹配文件名开头的数字
    match = re.match(r'^(\d+)', filename)
    if match:
        return int(match.group(1))
    return float('inf')  # 没有数字前缀的文件排在最后

def remove_number_prefix_from_filename(filename):
    """去掉文件名的数字前缀"""
    # 匹配并去掉 "数字-" 或 "数字｜" 格式的前缀
    cleaned = re.sub(r'^\d+[-｜]\s*', '', filename)
    return cleaned

def remove_number_prefix_from_title(title):
    """去掉标题的数字前缀"""
    # 去掉 "# 数字｜" 或 "# 数字-" 格式的前缀，保留 #
    cleaned = re.sub(r'^(#\s*)\d+[｜|-]\s*', r'\1', title)
    return cleaned

def get_title_from_content(content):
    """从文件内容中提取标题"""
    lines = content.split('\n')
    for line in lines:
        if line.strip().startswith('#'):
            return line.strip()
    return ""

def process_markdown_files(directory):
    """处理 markdown 文件"""
    directory = Path(directory)
    
    # 获取所有 .md 文件（排除 SUMMARY.md）
    md_files = [f for f in directory.glob('*.md') if f.name != 'SUMMARY.md']
    
    # 按数字前缀排序
    md_files.sort(key=lambda x: extract_number_from_filename(x.name))
    
    # 用于存储 SUMMARY.md 的内容
    summary_entries = []
    
    # 备份原始文件到临时目录
    backup_dir = directory / 'backup_original'
    if backup_dir.exists():
        shutil.rmtree(backup_dir)
    backup_dir.mkdir()
    
    print(f"正在处理 {len(md_files)} 个 markdown 文件...")
    
    for md_file in md_files:
        try:
            print(f"处理文件: {md_file.name}")
            
            # 备份原始文件
            shutil.copy2(md_file, backup_dir / md_file.name)
            
            # 读取文件内容
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 获取原始标题
            original_title = get_title_from_content(content)
            
            # 修改文件内容：去掉第一行标题的数字前缀
            lines = content.split('\n')
            if lines and lines[0].strip().startswith('#'):
                lines[0] = remove_number_prefix_from_title(lines[0])
                modified_content = '\n'.join(lines)
            else:
                modified_content = content
            
            # 生成新的文件名（去掉数字前缀）
            new_filename = remove_number_prefix_from_filename(md_file.name)
            new_file_path = directory / new_filename
            
            # 如果新文件名和原文件名不同，进行重命名
            if new_filename != md_file.name:
                # 先写入修改后的内容到新文件
                with open(new_file_path, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                
                # 删除原文件
                md_file.unlink()
                print(f"  重命名: {md_file.name} -> {new_filename}")
            else:
                # 文件名相同，只更新内容
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(modified_content)
                print(f"  更新内容: {md_file.name}")
            
            # 为 SUMMARY.md 准备条目
            clean_title = remove_number_prefix_from_title(original_title).replace('#', '').strip()
            if clean_title:
                summary_entries.append(f"- [{clean_title}](./{new_filename})")
            
        except Exception as e:
            print(f"处理文件 {md_file.name} 时出错: {e}")
            continue
    
    # 生成 SUMMARY.md
    summary_content = "# Summary\n\n" + "\n".join(summary_entries) + "\n"
    
    summary_path = directory / 'SUMMARY.md'
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    
    print(f"\n✅ 处理完成！")
    print(f"📝 生成了新的 SUMMARY.md，包含 {len(summary_entries)} 个条目")
    print(f"💾 原始文件已备份到: {backup_dir}")
    print(f"📋 SUMMARY.md 内容预览:")
    print("-" * 50)
    print(summary_content)

def main():
    """主函数"""
    current_dir = os.getcwd()
    print(f"当前工作目录: {current_dir}")
    print("开始整理 Markdown 文档...")
    
    try:
        process_markdown_files(current_dir)
    except Exception as e:
        print(f"❌ 处理过程中出现错误: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
