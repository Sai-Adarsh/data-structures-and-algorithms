class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": lambda x, y : x + y, 
            "-": lambda x, y : x - y,
            "*": lambda x, y : x * y,
            "/": lambda x, y : x / y
        }

        for i in range(len(tokens)):
            if tokens[i] in operators:
                operandOne = int(stack.pop())
                operandTwo = int(stack.pop())
                valToAppend = int(operators[tokens[i]](operandTwo, operandOne))
                stack.append(str(valToAppend))
            else:
                stack.append(tokens[i])

        return int(stack.pop())