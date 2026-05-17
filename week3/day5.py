import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

# 旅行先リスト
spots = [
    {"name": "沖縄", "price": "4万円〜", "feature": "青い海とサンゴ礁"},
    {"name": "京都", "price": "3万円〜", "feature": "紅葉と古都の風情"},
    {"name": "北海道", "price": "5万円〜", "feature": "雪景色と新鮮な海の幸"},
]

# for文で全スポットの投稿文を一括生成
for spot in spots:
    prompt = f"""旅行アフィリエイトブロガーとして、X投稿文を140文字以内で3パターン作成してください。

旅行先：{spot['name']}
価格帯：{spot['price']}
特徴：{spot['feature']}

番号をつけて3パターン出してください。"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    print(f"\n=== {spot['name']} ===")
    print(response.content[0].text)
    print("-" * 40)