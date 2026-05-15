# Week1 総まとめ練習問題
# 変数・リスト・if文・関数・ファイルを組み合わせて使う

# ===== 問題1 =====
# 旅行先リストを受け取って、
# 「国内」か「海外」かを判定して分類する関数を作ってください
# 関数名：classify_spots
#
# 国内リスト：["東京", "沖縄", "金沢", "北海道", "京都", "大阪"]
# 上記に含まれていれば「国内」、それ以外は「海外」
#
# 使い方：
#   my_list = ["東京", "パリ", "沖縄", "ニューヨーク", "金沢"]
#   classify_spots(my_list)
#
# 出力例：
#   === 旅行先分類 ===
#   東京 → 国内
#   パリ → 海外
#   沖縄 → 国内
#   ニューヨーク → 海外
#   金沢 → 国内

# ここに書く↓
def classify_spots(spots):
    domesutic = ["東京", "沖縄", "金沢", "北海道", "京都", "大阪"]

    print("=== 旅行先分類 ===")
    for spot in spots:
        if spot in domesutic:
            print(f"{spot}→国内")
        else:
            print(f"{spot}→海外")

my_list = ["東京", "パリ", "沖縄", "ニューヨーク", "金沢"]
classify_spots(my_list)

# ===== 問題2 =====
# 旅行プランをファイルに保存して、読み込んで表示する関数を作ってください
# 関数名：save_and_show
#
# 受け取るもの：旅行先（文字列）、泊数（数値）、予算（数値）
# ファイル名：trip_plan.txt
# 保存する内容：
#   旅行先：〇〇show
#   泊数：〇泊
#   予算：〇〇円
#   1泊あたり：〇〇円
#
# 使い方：save_and_show("沖縄", 3, 60000)
# 実行後に trip_plan.txt が作られ、内容を表示する

# ここに書く↓
def save_and_show(spot, nights, budget):
    per_night = budget // nights

    with open("trip_plan.txt", "w", encoding="utf-8") as f:
        f.write(f"旅行先：{spot}\n")
        f.write(f"泊数：{nights}泊\n")
        f.write(f"予算：{budget}円\n")
        f.write(f"1泊あたり：{per_night}円\n")

    with open("trip_plan.txt", "r", encoding="utf-8") as f:
        print(f.read())

save_and_show("沖縄", 3, 60000)


# ===== 問題3（応用）=====
# 旅行先リストをファイルから読み込んで、
# 予算に合わせておすすめを1件返す関数を作ってください
# 関数名：recommend
#
# spots.txt の中身（手動で作ってください）：
#   沖縄,50000
#   東京,20000
#   パリ,150000
#   金沢,30000
#
# 仕様：
#   - spots.txt を読み込む
#   - 各行を「旅行先,価格」に分割する（ヒント：split(",")）
#   - 予算以内で一番高い旅行先を返す
#
# 使い方：print(recommend(80000))
# 出力例：予算80,000円でおすすめ：沖縄（50,000円）

# ここに書く↓
def recommend(budget):
    best_spot = ""
    best_price = 0

    with open("spots.txt", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    for line in lines:
        parts = line.split(",")     # ["沖縄", "50000"]
        name  = parts[0]            # "沖縄"
        price = int(parts[1])       # 50000

        if price <= budget and price > best_price:
            best_spot  = name
            best_price = price

    return f"予算{budget:,}円でおすすめ：{best_spot}（{best_price:,}円）"

print(recommend(80000))