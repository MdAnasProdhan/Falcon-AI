from modules.greetings import GreetingsPlugin
from modules.calculator import CalculatorPlugin
from modules.time_tool import TimePlugin

plugins = [
    GreetingsPlugin(),
    CalculatorPlugin(),
    TimePlugin(),
]

def route(text):
    for plugin in plugins:
        result = plugin.handle(text)
        if result is not None:
            return result

    return None
