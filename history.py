import json
import os

FILE_NAME = "history.json"

def load_history():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_command(command):
    history = load_history()

    history.append(command)

    # শুধু শেষ 100টি কমান্ড রাখবে
    history = history[-100:]

    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)

def show_history():
    history = load_history()

    if not history:
        return "No command history."

    return "\n".join(history)
