#!/bin/bash

# 获取最新版本号
LATEST_VERSION=$(curl -s https://api.github.com/repos/rust-lang/mdBook/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')

# 移除版本号前的 'v'
MDBOOK_VERSION=${LATEST_VERSION#v}

echo "Latest mdBook version: $MDBOOK_VERSION"

# 下载并解压最新版本
curl -L "https://github.com/rust-lang/mdBook/releases/download/$LATEST_VERSION/mdbook-$LATEST_VERSION-x86_64-unknown-linux-gnu.tar.gz" | tar xvz

# 检查是否成功解压
if [ -f "./mdbook" ]; then
    echo "mdBook $MDBOOK_VERSION has been successfully downloaded and extracted."
    
    # 构建文档 
    ./mdbook build
else
    echo "Failed to download or extract mdBook."
    exit 1
fi
