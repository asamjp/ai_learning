# Week1 Day3 - if文（条件分岐）

# ① 基本のif文
budget = 100000  # 予算（円）

if budget >= 30000:
    print("海外旅行もOK！")
else:
    print("国内でお得に旅しよう！")

# ② elif で条件を増やす（else if の略）
print("\n=== 予算別おすすめ ===")

if budget >= 100000:
    print("ヨーロッパや長期旅行もいける！")
elif budget >= 50000:
    print("東南アジアや国内高級旅館がおすすめ！")
elif budget >= 30000:
    print("国内旅行や近場の海外がおすすめ！")
else:
    print("日帰り温泉や近場スポットを探そう！")

# ③ リストと組み合わせる
print("\n=== 旅行先チェック ===")
spots = ["沖縄", "アメリカ", "金沢", "東京", "大阪"]
target = "パリ"

if target in spots:
    print(f"{target} はリストに入ってます！")
else:
    print(f"{target} はまだリストにないです")
