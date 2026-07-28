from gemini import ask_gemini

class PlannerPlugin:

    def handle(self, text):

        if text.startswith("plan "):

            task = text[5:]

            prompt = f"""
Create a clear step-by-step plan for:

{task}

Use numbered steps.
Keep it short.
"""

            return ask_gemini(prompt)

        return None
