import json

# JSONに書き込む
travel_data = [
    {"name": "沖縄", "price": "4万円〜", "season": "夏", "score": 5},
    {"name": "京都", "price": "3万円〜", "season": "秋", "score": 4},
    {"name": "北海道", "price": "5万円〜", "season": "冬", "score": 5},
    {"name": "福岡", "price": "2万円〜", "season": "通年", "score": 4},
]

with open("travel_data.json", "w", encoding="utf-8") as f:
    json.dump(travel_data, f, ensure_ascii=False, indent=2)

print("JSON書き込み完了！")

# JSONを読み込む
with open("travel_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for spot in data:
    print(f"{spot['name']}：{spot['price']}　おすすめ度：{spot['score']}")