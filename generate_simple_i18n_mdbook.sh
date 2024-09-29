#!/bin/bash

# 安装 Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# 更新 PATH 以包含 Cargo
source $HOME/.cargo/env

# 安装 mdbook 及相关工具
cargo install mdbook
cargo install --locked mdbook-i18n


# 构建 mdbook
if [ -f "book.toml" ]; then
    echo "Building mdbook..."
    mdbook build
else
    echo "book.toml not found. Skipping mdbook build."
fi

echo "安装完成！"
