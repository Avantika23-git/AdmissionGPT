import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

def ask_llm(prompt):

    response = requests.post(

        "https://openrouter.ai/api/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },

        json={

            # Free model
            "model": "meta-llama/llama-3.2-3b-instruct:free",

            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

    )

    response.raise_for_status()

    return response.json()[
        "choices"
    ][0]["message"]["content"]