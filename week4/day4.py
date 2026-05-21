import anthropic
import sys
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

client = anthropic.Anthropic()

# =====================================================
# Day 4: コードを整理する
#
# Day 3 との違い：
# - データ・生成・表示 をそれぞれ別の関数に分けた
# - スポットを追加したいときは SPOTS リストだけ編集すればOK
# - generate_post() を呼ぶだけでどこからでも使える
# =====================================================

SPOTS = [
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
        "feature": "雪景色と新鮮な海の幸",
        "link": "https://px.a8.net/svt/ejp?a8mat=XXXXX&a8ejpredirect=https://www.jalan.net/",
    },
]


def generate_post(spot):
    """1つのスポット情報からX投稿文を生成して返す"""
    prompt = f"""旅行アフィリエイトブロガーとして、X（Twitter）の投稿文を作成してください。

旅行先: {spot['name']}
価格帯: {spot['price']}
おすすめシーズン: {spot['season']}
特徴: {spot['feature']}
予約リンク: {spot['link']}

条件:
- 140文字以内
- 最後にリンクを含める（URLをそのまま貼る）
- 読んだ人が行きたくなる文章
- ハッシュタグを2〜3個つける

投稿文のみ出力してください。"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def show_post(spot, post):
    """スポット名と投稿文を見やすく表示する"""
    print(f"【{spot['name']}】")
    print(post)
    print("-" * 40)


def main():
    print("=== 旅行アフィリエイト投稿文ジェネレーター ===\n")

    for spot in SPOTS:
        post = generate_post(spot)
        show_post(spot, post)


main()
