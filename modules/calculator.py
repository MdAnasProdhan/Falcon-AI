import ast
import operator

from modules.plugin import Plugin

OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

class CalculatorPlugin(Plugin):

    def __init__(self):
        super().__init__("Calculator")

    def calculate(self, node):

        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.BinOp):
            left = self.calculate(node.left)
            right = self.calculate(node.right)

            op = OPS[type(node.op)]

            return op(left, right)

        raise ValueError("Invalid expression")

    def handle(self, text):

        if text.startswith("calculate "):
            expression = text[10:]

        elif any(op in text for op in ["+", "-", "*", "/", "%", "**"]):
            expression = text

        else:
            return None

        try:
            tree = ast.parse(expression, mode="eval")
            return str(self.calculate(tree.body))

        except:
            return "Invalid calculation."
