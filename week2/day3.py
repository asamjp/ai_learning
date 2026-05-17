# ファイルの書き込み（w モード）
with open("travel_notes.txt", "w", encoding="utf-8") as f:
    f.write("沖縄：青い海が最高\n")
    f.write("京都：紅葉の季節がおすすめ\n")
    f.write("北海道：ラーメンと雪景色\n")

print("書き込み完了！")

# ファイルの読み込み（r モード）
with open("travel_notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("読み込んだ内容：")
print(content)

# 追記（a モード）
with open("travel_notes.txt", "a", encoding="utf-8") as f:
    f.write("福岡：博多ラーメンと屋台\n")

print("追記完了！")

# もう一度読み込んで確認
with open("travel_notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())