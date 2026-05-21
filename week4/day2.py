# Week 4 Day 2: アフィリエイトリンクの仕組みを理解する

# =====================================================
# アフィリエイトリンクとは？
# =====================================================
#
# 通常のURL: https://www.jalan.net/yad123456/
# アフィリエイトURL: https://px.a8.net/svt/ejp?a8mat=xxxxxxxx&a8ejpredirect=https://www.jalan.net/yad123456/
#
# 仕組み：
# 1. ユーザーがアフィリエイトURLをクリック
# 2. A8.netのサーバーを経由（ここでクリックが記録される）
# 3. じゃらんのページに飛ぶ
# 4. ユーザーが予約したら → 自分に報酬が入る！
# =====================================================

# --- Step 1: アフィリエイトリンクを変数に保存する ---

# ※ 実際のリンクはA8.netやバリューコマースの管理画面から取得する
# ※ 今日は練習用のダミーURLを使います

affiliate_links = {
    "じゃらん": "https://px.a8.net/svt/ejp?a8mat=XXXXX&a8ejpredirect=https://www.jalan.net/",
    "楽天トラベル": "https://ck.jp.ap.valuecommerce.com/servlet/referral?sid=XXXXX&pid=XXXXX&vc_url=https://travel.rakuten.co.jp/",
    "Hotels.com": "https://px.a8.net/svt/ejp?a8mat=YYYYY&a8ejpredirect=https://jp.hotels.com/",
}

print("=== 登録済みアフィリエイトリンク ===")
for service, url in affiliate_links.items():
    print(f"【{service}】")
    print(f"  URL: {url}")
    print()


# --- Step 2: リンクを使いやすい関数にする ---

def get_affiliate_link(service_name):
    """サービス名からアフィリエイトリンクを返す"""
    if service_name in affiliate_links:
        return affiliate_links[service_name]
    else:
        return None


# 使い方を確認
link = get_affiliate_link("じゃらん")
print(f"じゃらんのリンク: {link}")

link2 = get_affiliate_link("存在しないサービス")
print(f"存在しないサービス: {link2}")  # None が返る


# --- Step 3: 旅行スポット情報にリンクを組み込む ---

spots = [
    {
        "name": "沖縄",
        "price": "2泊3日 4万円〜",
        "season": "通年（特に3〜5月）",
        "feature": "青い海とサンゴ礁",
        "booking_site": "じゃらん",
    },
    {
        "name": "京都",
        "price": "2泊3日 3万円〜",
        "season": "11月（紅葉シーズン）",
        "feature": "紅葉と古都の風情",
        "booking_site": "楽天トラベル",
    },
    {
        "name": "北海道",
        "price": "2泊3日 5万円〜",
        "season": "2月（雪まつり）",
        "feature": "雪景色と新鮮な海の幸",
        "booking_site": "じゃらん",
    },
]

print("\n=== 旅行スポット一覧（アフィリエイトリンク付き）===")
for spot in spots:
    link = get_affiliate_link(spot["booking_site"])
    print(f"【{spot['name']}】")
    print(f"  価格: {spot['price']}")
    print(f"  おすすめシーズン: {spot['season']}")
    print(f"  特徴: {spot['feature']}")
    print(f"  予約リンク: {link}")
    print()
