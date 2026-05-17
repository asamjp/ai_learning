import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

# 普通に聞く
response1 = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "沖縄について教えて"}
    ]
)
print("=== 普通に聞いた場合 ===")
print(response1.content[0].text)

# 旅行ブロガーとして書いてもらう
response2 = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "あなたは人気旅行ブロガーです。沖縄の魅力をX（Twitter）投稿風に140文字以内で書いてください。"}
    ]
)
print("\n=== 旅行ブロガーとして ===")
print(response2.content[0].text)