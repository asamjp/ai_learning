# Day4 練習問題

# ===== 問題1 =====
# 旅行先を受け取って「〇〇への旅、楽しんできてね！」と返す関数を作ってください
# 関数名：send_off
# 使い方：print(send_off("沖縄"))
# 出力例：沖縄への旅、楽しんできてね！

# ここに書く↓
def send_off(sopt):
    return f"{sopt}への旅、楽しんできてね！"

print(send_off("沖縄"))
print(send_off("東京"))
print(send_off("京都"))

# ===== 問題2 =====
# 泊数を受け取って、料金を計算して返す関数を作ってください
# 1泊あたり8,000円とする
# 関数名：calc_price
# 使い方：print(calc_price(3))
# 出力例：3泊の料金は24,000円です

# ここに書く↓
def calc_price(nights):
    total=nights * 8000
    return f"{nights}泊の料金は{total}円です"

print(calc_price(3))
print(calc_price(4))
print(calc_price(3))

# ===== 問題3（応用）=====
# 旅行先リストを受け取って、件数と一覧を表示する関数を作ってください
# 関数名：show_list
# 使い方：
#   spots = ["沖縄", "金沢", "パリ"]
#   show_list(spots)
# 出力例：
#   全部で3か所あります
#   1. 沖縄
#   2. 金沢
#   3. パリ

# ここに書く↓
def show_list(spots):
    print (f"全部で{len(spots)}か所あります")
    for i, spot in enumerate(spots, 1):
        print(f"{i}. {spot}")

spots = ["沖縄", "金沢", "パリ"]
show_list(spots)