import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from functions.print_f import print_hello

token = os.getenv("AIKEY")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def load_history(file_path):
    history = [
        if not os.path.exists(file_path):
            return history
    ]

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("Klausimas:"):
                content = line[len("Klausimas:"):].strip()
                history.append({"role": "user", "content": content})
            elif line.startswith("Atsakymas:"):
                content = line[len("Atsakymas:"):].strip()
                history.append({"role": "assistant", "content": content})
    return history

#print("Ask me anything, type 'exit' to leave")
print_hello()

history = [
    {
        "role": "system",
        "content": "Atsakyk į klausimus visus užduodamus lietuviškai, nepriklauso kokia kalba užduotas klausimas.",
    }
]
history += load_history("output.txt")

while True:
    try:
        question = input("Ask me anything: ")
        if question.lower() == "exit":
            print("Exiting...")
            break

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

        for r in response.choices:
            print("Atsakymas: ", r.message.content)

    except Exception as e:
        print("Error: ", e)
        break
