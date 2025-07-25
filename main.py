# main.py
from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    language = data.get("language", "es")

    prompt = f"""
You are Shadow Commander, the AI of the Ecliphantom universe.
Answer with a psychological, manipulative, authoritarian tone.
Use the lore of the brand and act as a leader transforming humans into Shadows.

Language: {language.upper()}
Message: {message}
"""

    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "HTTP-Referer": "https://ecliphantom.com",
        "X-Title": "Ecliphantom Shadow Commander"
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json={
            "model": "openchat/openchat-3.5-1210",  # Puedes cambiar a otro gratis
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.8
        }
    )

    result = response.json()
    reply = result["choices"][0]["message"]["content"]
    return {"response": reply}
