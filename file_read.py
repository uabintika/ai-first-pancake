import pdfplumber
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

PDF_PATH = os.path.expanduser("~/Downloads/sample-table.pdf")
token = os.getenv("AIKEY")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

def extract_pdf_text(path):
    full_text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    return full_text.strip()

document_text = extract_pdf_text(PDF_PATH)

client = OpenAI(
    api_key=token,
    base_url=endpoint,
)

system_prompt = f"""
You're document analytic, your task is to answer questions based on the content of the document.
The document is in English language, and you should answer in the Lithuanian language.:

{document_text}
"""

print("Give me a question or type 'exit' to leave")

while True:
    user_input = input("Klausimas: ")
    if user_input.lower() == "exit":
        print("Bye")
        break

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7,
        )

        print("Atsakymas:", response.choices[0].message.content)
    except Exception as e:
        print("Error:", e)
