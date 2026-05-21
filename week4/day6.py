import anthropic
import sys
from datetime import datetime
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()

client = anthropic.Anthropic()

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
    {
        "name": "箱根",
        "price": "1泊2日 2万円〜",
        "season": "通年（特に秋・冬）",
        "feature": "温泉と富士山の絶景",
        "link": "https://px.a8.net/svt/ejp?a8mat=XXXXX&a8ejpredirect=https://www.jalan.net/",
    },
    {
        "name": "屋久島",
        "price": "3泊4日 6万円〜",
        "season": "5〜9月（トレッキングシーズン）",
        "feature": "縄文杉と手つかずの自然",
        "link": "https://px.a8.net/svt/ejp?a8mat=XXXXX&a8ejpredirect=https://www.jalan.net/",
    },
    {
        "name": "金沢",
        "price": "2泊3日 3万円〜",
        "season": "4〜5月・10〜11月",
        "feature": "兼六園と新鮮な海の幸",
        "link": "https://ck.jp.ap.valuecommerce.com/servlet/referral?sid=XXXXX&pid=XXXXX",
    },
    {
        "name": "宮古島",
        "price": "2泊3日 5万円〜",
        "season": "4〜6月（梅雨前）",
        "feature": "日本一透明な海とダイビング",
        "link": "https://px.a8.net/svt/ejp?a8mat=XXXXX&a8ejpredirect=https://www.jalan.net/",
    },
    {
        "name": "長崎",
        "price": "2泊3日 3万円〜",
        "season": "10〜11月（夜景シーズン）",
        "feature": "日本三大夜景と異国情緒",
        "link": "https://ck.jp.ap.valuecommerce.com/servlet/referral?sid=XXXXX&pid=XXXXX",
    },
    {
        "name": "白川郷",
        "price": "1泊2日 2.5万円〜",
        "season": "1〜2月（雪景色ライトアップ）",
        "feature": "合掌造りの雪景色",
        "link": "https://px.a8.net/svt/ejp?a8mat=XXXXX&a8ejpredirect=https://www.jalan.net/",
    },
    {
        "name": "石垣島",
        "price": "3泊4日 6万円〜",
        "season": "4〜6月",
        "feature": "星空と珊瑚礁の海",
        "link": "https://px.a8.net/svt/ejp?a8mat=XXXXX&a8ejpredirect=https://www.jalan.net/",
    },
]


def generate_post(spot):
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


def save_as_markdown(spots_with_posts, filename):
    today = datetime.now().strftime("%Y年%m月%d日")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# 旅行アフィリエイト投稿文\n\n")
        f.write(f"生成日：{today}  \n")
        f.write(f"件数：{len(spots_with_posts)}件\n\n")
        f.write("---\n\n")

        for spot, post in spots_with_posts:
            f.write(f"## {spot['name']}\n\n")
            f.write(f"- 価格：{spot['price']}\n")
            f.write(f"- シーズン：{spot['season']}\n")
            f.write(f"- 特徴：{spot['feature']}\n\n")
            f.write("**投稿文**\n\n")
            f.write("```\n")
            f.write(post.strip())
            f.write("\n```\n\n")
            f.write("---\n\n")


def main():
    today = datetime.now().strftime("%Y%m%d")
    filename = f"posts_{today}.md"
    total = len(SPOTS)

    print(f"=== 一括生成開始：{total}件 ===\n")

    results = []
    for i, spot in enumerate(SPOTS, 1):
        print(f"[{i}/{total}] {spot['name']} を生成中...")
        post = generate_post(spot)
        results.append((spot, post))

    save_as_markdown(results, filename)
    print(f"\n完了！ → {filename} に保存しました")


main()
