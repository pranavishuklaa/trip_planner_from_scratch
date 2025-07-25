from langchain.tools import tool

class CalculatorTools():

    @tool("Make a calculation")

    def calculate(self, operation):
        """ Useful to perform any mathematical calculations,
        like sum, minus, multiplication, division, etc
        The input to this tool should be a mathematical
        expresion, a couple examples are `200*7` or `5000/7*10'
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid math syntax"


