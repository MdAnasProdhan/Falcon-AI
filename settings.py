import json
import os

FILE_NAME = "settings.json"

DEFAULT_SETTINGS = {
    "name": "Anas",
    "language": "bn",
    "voice": False,
    "dark_mode": False
}

def load_settings():
    if not os.path.exists(FILE_NAME):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS

    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_settings(settings):
    with open(FILE_NAME, "w") as file:
        json.dump(settings, file, indent=4)
