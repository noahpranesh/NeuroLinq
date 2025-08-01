import tkinter as tk
import requests

def chat():
    user_input = entry.get()
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)

    # Send to model
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "tinyllama",
            "prompt": user_input,
            "stream": False
        }
    )

    model_reply = response.json()["response"]
    chat_log.insert(tk.END, "NeuroLink1: " + model_reply + "\n\n")

# GUI setup
root = tk.Tk()
root.title("NeuroLink1 Chatbot")

chat_log = tk.Text(root, bg="black", fg="lime", font=("Consolas", 12))
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Consolas", 12))
entry.pack(padx=10, pady=5, fill=tk.X)
entry.bind("<Return>", lambda event: chat())

send_button = tk.Button(root, text="Send", command=chat)
send_button.pack(pady=5)

root.mainloop()
