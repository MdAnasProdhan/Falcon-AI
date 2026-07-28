from datetime import datetime
import os

LOG_FILE = "logs/falcon.log"

def log(message):
    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")
