from datetime import datetime
from modules.plugin import Plugin

class TimePlugin(Plugin):

    def __init__(self):
        super().__init__("Time")

    def handle(self, text):

        if text == "time":
            return "Current time: " + datetime.now().strftime("%I:%M:%S %p")

        if text == "date":
            return "Today's date: " + datetime.now().strftime("%d-%m-%Y")

        return None
