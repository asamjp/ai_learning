# Day4 練習問題2

# ===== 問題4 =====
# 旅行先と泊数を両方受け取って、まとめた文を返す関数を作ってください
# 1泊8,000円で計算する
# 関数名：trip_plan
# 使い方：print(trip_plan("沖縄", 3))
# 出力例：沖縄に3泊するなら、24,000円かかります

# ここに書く↓
def trip_plan(trip , nights):
    total = nights * 8000
    return f"{trip}に{nights}泊するなら、{total}円かかります"

print(trip_plan("沖縄", 3))

# ===== 問題5 =====
# リストを受け取って「一番行きたいのは〇〇です」と返す関数を作ってください
# リストの1番目（先頭）を「一番行きたい場所」とする
# 関数名：top_spot
# 使い方：
#   spots = ["沖縄", "パリ", "金沢"]
#   print(top_spot(spots))
# 出力例：一番行きたいのは沖縄です

# ヒント：リストの1番目は spots[0] で取れます

# ここに書く↓
def top_spot(spot):
    return f"一番行きたいのは{spots[0]}です"

spots = ["沖縄", "パリ", "金沢"]
print(top_spot(spots))

# ===== 問題6（応用）=====
# 予算と泊数を受け取って、行けるかどうか判定する関数を作ってください
# 1泊8,000円で計算する
# 関数名：can_go
# 使い方：print(can_go(30000, 3))
# 出力例（予算が足りる場合）：OK！予算30,000円で3泊できます
# 出力例（予算が足りない場合）：予算が足りません。あと6,000円必要です

# ヒント：必要金額 = 泊数 × 8000、不足額 = 必要金額 - 予算

# ここに書く↓
def can_go(budget,nights):
    if budget >=  nights * 8000: 
        print(f"OK！予算{budget}円で{nights}泊できます")
    else:
        shortfall = ( nights * 8000) - budget
        print(f"予算が足りません。あと{shortfall}円必要です")

can_go(30000, 3)   # ← ファイルの末尾に追加
can_go(10000, 3)  # 足りないパターンも試す