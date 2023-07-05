class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for i in range(len(tokens)):
            if tokens[i] in operators:
                operandOne = stack.pop()
                operandTwo = stack.pop()
                stack.append(str(int(eval(operandTwo + tokens[i] + operandOne))))
            else:
                stack.append(tokens[i])

        return int(stack.pop())