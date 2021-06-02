class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")":
                res = []
                while stack and stack[-1] != "(":
                    res.append(stack.pop())
                stack.pop()
                stack += res
            else:
                stack.append(i)
                
        return "".join(stack)