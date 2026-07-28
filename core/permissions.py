PROTECTED_COMMANDS = [
    "complete delivery",
    "send money",
    "delete file",
    "confirm order"
]

def requires_permission(text):
    text = text.lower().strip()

    for command in PROTECTED_COMMANDS:
        if text.startswith(command):
            return True

    return False
