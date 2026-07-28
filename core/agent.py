from brain import think

class FalconAgent:

    def process(self, user_input):
        return think(user_input)

    def status(self):
        return """Falcon Agent

Modules:
✓ Calculator
✓ Memory
✓ Notes
✓ Planner
✓ Gemini
✓ History
✓ Logger
"""
