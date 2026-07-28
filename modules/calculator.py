from modules.plugin import Plugin

class CalculatorPlugin(Plugin):

    def __init__(self):
        super().__init__("Calculator")

    def handle(self, text):

        if not text.startswith("calculate "):
            return None

        expression = text[10:]

        try:
            return str(eval(expression))
        except:
            return "Invalid calculation."
