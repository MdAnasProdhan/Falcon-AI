from core.permissions import requires_permission
from settings import load_settings
from history import save_command
from brain import think
from core.logger import log

settings = load_settings()

print("=" * 40)
print("🦅 Falcon AI")
log("Falcon AI started.")
print("=" * 40)
print(f"User : {settings['name']}")
print(f"Language : {settings['language']}")
print("=" * 40)

while True:
    user = input("You: ")

    if requires_permission(user):
        answer = input("⚠️ Permission required (yes/no): ")

        if answer.lower() != "yes":
            print("Falcon AI: Action cancelled.")
            continue

    log(f"User: {user}")
    save_command(user)

    if user.lower() == "exit":
        print("Falcon AI: Goodbye!")
        break

    reply = think(user)
    log(f"Falcon AI: {reply}")
    print("Falcon AI:", reply)
