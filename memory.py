import json
import os

FILE_NAME = "memory.json"

def load_name():
    if not os.path.exists(FILE_NAME):
        return None

    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    return data.get("name")

def save_name(name):
    data = {
        "name": name
    }

    with open(FILE_NAME, "w") as file:
        json.dump(data, file)
