import anthropic
import sys
from dotenv import load_dotenv

# Windows で絵文字を含む文字列を表示できるようにする
sys.stdout.reconfigure(encoding="utf-8")

load_dotenv()

client = anthropic.Anthropic()

# --- Day 2で作ったデータ（link も追加）---

spots = [
    {
        "name": "沖縄",
        "price": "2泊3日 4万円〜",
        "season": "通年（特に3〜5月）",
        "feature": "青い海とサンゴ礁",
        "link": "https://px.a8.net/svt/ejp?a8mat=XXXXX&a8ejpredirect=https://www.jalan.net/",
    },
    {
        "name": "京都",
        "price": "2泊3日 3万円〜",
        "season": "11月（紅葉シーズン）",
        "feature": "紅葉と古都の風情",
        "link": "https://ck.jp.ap.valuecommerce.com/servlet/referral?sid=XXXXX&pid=XXXXX",
    },
    {
        "name": "北海道",
        "price": "2泊3日 5万円〜",
        "season": "2月（雪まつり）",
        "feature": "雪景色と新鮮な海の鮮",
        "link": "https://px.a8.net/svt/ejp?a8mat=XXXXX&a8ejpredirect=https://www.jalan.net/",
    },
]


# --- Claudeに投稿文を生成させる関数 ---

def generate_post(spot):
    prompt = f"""旅行アフィリエイトブロガーとして、X（Twitter）の投稿文を作成してください。

旅行先: {spot['name']}
価格帯: {spot['price']}
おすすめシーズン: {spot['season']}
特徴: {spot['feature']}
予約リンク: {spot['link']}

条件:
- 140文字以内
- 最後にリンクを含める（リンクはURLをそのまま貼る）
- 読んだ人が行きたくなる文章
- ハッシュタグを2〜3個つける

投稿文のみ出力してください。"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


# --- 全スポット分を生成して表示 ---

print("=== アフィリエイトリンク付き投稿文 ===\n")

for spot in spots:
    print(f"【{spot['name']}】")
    post = generate_post(spot)
    print(post)
    print("-" * 40)
