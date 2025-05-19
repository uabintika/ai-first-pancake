import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("AIKEY")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

question = input("Ask me anything: ")

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Atsakyk į klausimus visus užduodamus lietuviškai, nepriklauso kokia kalba užduotas klausimas.",
        },
        {
            "role": "user",
            "content": question,
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

print(response.choices[0].message.content)

