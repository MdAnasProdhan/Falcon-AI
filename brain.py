from gemini import ask_gemini
from router import route
from notes import add_note, show_notes
from history import show_history

def think(user_input):
    text = user_input.lower().strip()

    if text == "history":
        return show_history()

    if text.startswith("note "):
        add_note(user_input[5:])
        return "Note saved."

    if text == "show notes":
        return show_notes()

    if text.startswith("ask "):
        question = user_input[4:]
        return ask_gemini(question)
        result = route(text)

    if result is not None:
        return result

    return "Sorry, I don't understand that yet."
