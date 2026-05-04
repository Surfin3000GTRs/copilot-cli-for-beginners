#!/bin/bash

# コミットメッセージを自動生成
COMMIT_MSG=$(copilot -p "次の差分に対するコミットメッセージを生成してください: $(git diff --staged)")
git commit -m "$COMMIT_MSG"

# ファイルレビュー
copilot --allow-all -p "@myfile.py の問題点をレビューしてください"
