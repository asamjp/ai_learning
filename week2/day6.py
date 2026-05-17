import json
import os

FILENAME = "spots.json"

def load_spots():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_spots(spots):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(spots, f, ensure_ascii=False, indent=2)

def add_spot(name, price, season, memo):
    spots = load_spots()
    spots.append({
        "name": name,
        "price": price,
        "season": season,
        "memo": memo
    })
    save_spots(spots)
    print(f"{name} を追加しました！")

def show_spots():
    spots = load_spots()
    if not spots:
        print("データがありません")
        return
    for spot in spots:
        print(f"\n【{spot['name']}】")
        print(f"  価格：{spot['price']}")
        print(f"  シーズン：{spot['season']}")
        print(f"  メモ：{spot['memo']}")

# 旅行先を追加
add_spot("沖縄", "4万円〜", "夏", "青い海が最高")
add_spot("京都", "3万円〜", "秋", "紅葉が綺麗")
add_spot("北海道", "5万円〜", "冬", "雪景色とラーメン")

# 一覧表示
print("\n=== 旅行スポット一覧 ===")
show_spots()