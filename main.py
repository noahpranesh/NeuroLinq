from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Optional: allow frontend to connect (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(message: Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change this to gpt-4 if you have access
            messages=[
                {"role": "user", "content": message.message}
            ]
        )
        reply = response.choices[0].message.content.strip()
        return {"response": reply}
    except Exception as e:
        return {"error": str(e)}
