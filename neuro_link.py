# NeuroLink1.py

import requests

def chat_with_mistral(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

print("💬 NeuroLink1 is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    reply = chat_with_mistral(user_input)
    print(f"NeuroLink1: {reply}\n")
