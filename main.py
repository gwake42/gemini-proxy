import os
import requests
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gemini API key and endpoint
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GEMINI_API_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

# Load MapsIndoors context from .txt file
mapsindoors_text = ""
try:
    with open("mapsindoors.txt", "r", encoding="utf-8") as f:
        mapsindoors_text = f.read()
    print("✅ Loaded MapsIndoors context from mapsindoors.txt")
except Exception as e:
    print(f"❌ Failed to load MapsIndoors context: {e}")

class Prompt(BaseModel):
    prompt: str

@app.post("/ask")
def ask_model(prompt: Prompt):
    headers = {
        "Content-Type": "application/json"
    }

    full_prompt = f"""
You are a helpful assistant trained on MapsIndoors. Use the following context to guide your answers. If you do not know the answer, ask the user for more information. 

Context:
{mapsindoors_text}

User query:
{prompt.prompt}
"""

    payload = {
        "contents": [
            {
                "parts": [{"text": full_prompt}]
            }
        ]
    }

    response = requests.post(GEMINI_API_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()
    try:
        text_response = data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        text_response = "❌ Failed to get a proper response from Gemini."

    return {"response": text_response}