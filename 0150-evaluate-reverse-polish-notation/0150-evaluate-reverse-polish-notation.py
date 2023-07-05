class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        def retNewOperand(operandOne, operandTwo, operator):
            if operator == "+":
                return int(operandTwo + operandOne)
            elif operator == "-":
                return int(operandTwo - operandOne)
            elif operator == "*":
                return int(operandTwo * operandOne)
            elif operator == "/":
                return int(operandTwo / operandOne)

        for i in range(len(tokens)):
            if tokens[i] in operators:
                operandOne = int(stack.pop())
                operandTwo = int(stack.pop())
                valToAppend = retNewOperand(operandOne, operandTwo, tokens[i])
                stack.append(str(valToAppend))
            else:
                stack.append(tokens[i])

        return int(stack.pop())