# scripts
useful scripts to make mdbook

* for py files you should run `python3 xxx.py`
*  for .sh you can use `curl -sSL https://raw.githubusercontent.com/read-x/scripts/refs/heads/main/xxxx.sh | bash`

# cf pages
+ build command
  ```bash
  curl -L https://github.com/rust-lang/mdBook/releases/download/v$MDBOOK_VERSION/mdbook-v$MDBOOK_VERSION-x86_64-unknown-linux-gnu.tar.gz | tar xvz && ./mdbook build
  ```
  output set `book`
  
  env `MDBOOK_VERSION` to `0.4.52`
  
