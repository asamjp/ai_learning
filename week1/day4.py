# Week1 Day4 - 関数（def）

# ① 基本の関数
def greet_spot(spot):
    return f"{spot}、いいですね！ぜひ行ってみてください！"

# 呼び出す
print(greet_spot("沖縄"))
print(greet_spot("パリ"))
print(greet_spot("金沢"))

# ② 引数を2つ受け取る関数
def trip_summary(spot, budget):
    if budget >= 50000:
        rank = "余裕あり"
    elif budget >= 20000:
        rank = "ちょうどいい"
    else:
        rank = "節約旅行"

    return f"【{spot}】予算{budget:,}円 → {rank}"

print("\n=== 旅行サマリー ===")
print(trip_summary("北海道", 100000))
print(trip_summary("東京", 25000))
print(trip_summary("近場", 8000))

# ③ リストと組み合わせる
def print_all_spots(spots):
    print("\n=== 旅行先リスト ===")
    for i, spot in enumerate(spots, 1):
        print(f"{i}. {spot}")

my_spots = ["沖縄", "アメリカ", "金沢", "東京", "大阪"]
print_all_spots(my_spots)
