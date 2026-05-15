# Week1 Day5 - ファイルの読み書き

# ① ファイルに書き込む（w = write）
print("=== ① ファイルに書き込む ===")
with open("travel_memo.txt", "w", encoding="utf-8") as f:
    f.write("沖縄\n")
    f.write("アメリカ\n")
    f.write("金沢\n")

print("travel_memo.txt に保存しました")

# ② ファイルを読み込む（r = read）
print("\n=== ② ファイルを読み込む ===")
with open("travel_memo.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)

# ③ 1行ずつリストとして読み込む
print("=== ③ 1行ずつ読み込む ===")
with open("travel_memo.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()  # 改行を除いてリストにする

for spot in lines:
    print(f"・{spot}")

# ④ 追記する（a = append）
print("\n=== ④ 追記する ===")
with open("travel_memo.txt", "a", encoding="utf-8") as f:
    f.write("パリ\n")

print("パリを追加しました")

# 追記後に再度読み込んで確認
with open("travel_memo.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

print(f"現在のリスト：{lines}")
