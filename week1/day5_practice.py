# Day5 練習問題 - ファイルの読み書き

# ===== 問題1 =====
# 自分の旅行先リストを my_spots.txt に保存してください
# 旅行先は最低3つ書くこと
# 使い方：実行すると my_spots.txt が作られる
#
# ヒント：
#   with open("my_spots.txt", "w", encoding="utf-8") as f:
#       f.write("〇〇\n")

# ここに書く↓
with open("my_spots.txt", "w", encoding="utf-8") as f:
    f.write("東京\n")
    f.write("フランス\n")
    f.write("金沢\n")

print("my_spots.txt に保存しました")

# ===== 問題2 =====
# my_spots.txt を読み込んで、1行ずつ表示してください
# 出力例：
#   === 私の旅行先リスト ===
#   1. 沖縄
#   2. アメリカ
#   3. 金沢
#
# ヒント：
#   lines = f.read().splitlines() でリストにしてから enumerate で番号をつける

# ここに書く↓
print("=== ③ 1行ずつ読み込む ===")
with open("my_spots.txt", "r", encoding="utf-8") as f:
   lines = f.read().splitlines() 

for spot in lines:
    print(f"{spot}")

# ===== 問題3 =====
# 新しい旅行先を1つ my_spots.txt に追記して、
# 追記後のリストを全件表示してください
#
# ヒント：追記は "a" モード

# ここに書く↓
print("\n=== ④ 追記する ===")
with open("my_spots.txt", "a", encoding="utf-8") as f:
    f.write("パリ\n")

# ===== 問題4（応用）=====
# my_spots.txt を読み込んで、
# 「〇〇への旅、楽しんできてね！」と全件表示する関数を作ってください
# 関数名：read_and_greet
# 使い方：read_and_greet("my_spots.txt")
#
# ヒント：Day4の send_off 関数とファイル読み込みを組み合わせる

# ここに書く↓
def read_and_greet(filename):
    with open(filename, "r", encoding="utf-8")as f:
        lines = f.read().splitlines()
        for spot in lines:
         print(f"{spot}への旅、楽しんできてね！")

read_and_greet("my_spots.txt")