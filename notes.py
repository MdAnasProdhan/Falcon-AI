import os

FILE_NAME = "notes.txt"

def add_note(note):
    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

def show_notes():
    if not os.path.exists(FILE_NAME):
        return "No notes found."

    with open(FILE_NAME, "r") as file:
        notes = file.read().strip()

    if notes == "":
        return "No notes found."

    return notes
