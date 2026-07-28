from modules.plugin import Plugin

class GreetingsPlugin(Plugin):

    def __init__(self):
        super().__init__("Greetings")

    def handle(self, text):

        if text == "hello":
            return "Hello! How can I help you?"

        if text == "hi":
            return "Hi!"

        if text == "bye":
            return "Goodbye!"

        return None
