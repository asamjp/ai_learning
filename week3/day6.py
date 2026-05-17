import anthropic
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = anthropic.Anthropic()

spots = [
    {"name": "沖縄", "price": "4万円〜", "feature": "青い海とサンゴ礁"},
    {"name": "京都", "price": "3万円〜", "feature": "紅葉と古都の風情"},
    {"name": "北海道", "price": "5万円〜", "feature": "雪景色と新鮮な海の幸"},
]

today = datetime.now().strftime("%Y%m%d")
filename = f"posts_{today}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"=== 旅行投稿文 {today} ===\n\n")

    for spot in spots:
        prompt = f"""旅行アフィリエイトブロガーとして、X投稿文を140文字以内で作成してください。

旅行先：{spot['name']}
価格帯：{spot['price']}
特徴：{spot['feature']}

投稿文のみ出力してください。"""

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )

        f.write(f"【{spot['name']}】\n")
        f.write(response.content[0].text)
        f.write("\n\n")
        print(f"{spot['name']} 完了")

print(f"\n{filename} に保存しました！")