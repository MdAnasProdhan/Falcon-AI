import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"

def ask_gemini(prompt):

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(
        URL,
        headers=headers,
        json=data,
        timeout=60
    )

    if response.status_code != 200:
        return f"API Error: {response.status_code}\n{response.text}"

    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"]
