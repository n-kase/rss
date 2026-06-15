import glob, re

count = 0
for f in glob.glob("/home/naoki.kase/.openclaw/workspace/rss/content/posts/post-*.md"):
    with open(f, "r") as file:
        content = file.read()
    
    # 意図せず入ってしまった「\n」という文字列（バックスラッシュ+n）を完全に削除する
    # これはbashエスケープの問題で混入したものです
    if "\\n" in content:
        # まず単独の行にある \n を削除
        new_content = re.sub(r"^\s*\\n\s*$", "", content, flags=re.MULTILINE)
        # それ以外の場所にある \n も削除
        new_content = new_content.replace("\\n", "")
        
        # 不要になった過剰な改行を整理
        new_content = re.sub(r"\n{3,}", "\n\n", new_content)
        
        if new_content != content:
            with open(f, "w") as file:
                file.write(new_content)
            count += 1

print(f"Removed literal \\n from {count} files.")
