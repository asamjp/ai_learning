import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

# 旅行情報を変数で管理
destination = "京都"
price = "3万円〜"
feature = "紅葉が美しい古都、金閣寺や嵐山が有名"

# 変数をプロンプトに埋め込む
prompt = f"""あなたは旅行アフィリエイトブロガーです。
以下の旅行情報をもとに、X（Twitter）投稿文を140文字以内で作成してください。

旅行先：{destination}
価格帯：{price}
特徴：{feature}

ハッシュタグも含めてください。"""

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(f"=== {destination}の投稿文 ===")
print(response.content[0].text)