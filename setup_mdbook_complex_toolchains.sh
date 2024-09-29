#!/bin/bash

# 安装 Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# 更新 PATH 以包含 Cargo
source $HOME/.cargo/env

# 安装 mdbook 及相关工具
cargo install mdbook
cargo install --locked mdbook-svgbob
cargo install --locked mdbook-i18n-helpers
cargo install --locked i18n-report
cargo install --locked mdbook-linkcheck

# 安装 mdbook-exerciser（如果目录存在）
if [ -d "./mdbook-exerciser" ]; then
    echo "Installing mdbook-exerciser..."
    cargo install --locked --path ./mdbook-exerciser
else
    echo "mdbook-exerciser directory not found. Skipping installation."
fi

# 安装 mdbook-course（如果目录存在）
if [ -d "./mdbook-course" ]; then
    echo "Installing mdbook-course..."
    cargo install --locked --path ./mdbook-course
else
    echo "mdbook-course directory not found. Skipping installation."
fi

# 构建 mdbook
if [ -f "book.toml" ]; then
    echo "Building mdbook..."
    mdbook build
else
    echo "book.toml not found. Skipping mdbook build."
fi

echo "安装完成！"
