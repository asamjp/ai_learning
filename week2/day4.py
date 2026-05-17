import csv

# CSVに書き込む
with open("travel_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["旅行先", "価格帯", "おすすめ度"])
    writer.writerow(["沖縄", "4万円〜", 5])
    writer.writerow(["京都", "3万円〜", 4])
    writer.writerow(["北海道", "5万円〜", 5])
    writer.writerow(["福岡", "2万円〜", 4])

print("CSV書き込み完了！")

# CSVを読み込む
with open("travel_data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)