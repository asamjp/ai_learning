# Week1 Day2 - リストとfor文

# ① リスト：複数の旅行先をまとめて入れる
spots = ["沖縄", "アメリカ", "金沢", "東京", "大阪"]

# ② for文：リストを1つずつ取り出して処理する
print("=== 行きたい旅行先リスト ===")
for spot in spots:
    print(f"・{spot}")

# ③ 旅行先の数を数える
print(f"\n合計 {len(spots)} か所")

# ④ 応用：文章と組み合わせる
print("\n=== おすすめ旅行先 ===")
for spot in spots:
    print(f"{spot}はおすすめの旅行先です！")
