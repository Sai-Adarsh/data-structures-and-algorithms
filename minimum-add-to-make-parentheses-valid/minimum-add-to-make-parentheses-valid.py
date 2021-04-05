class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        
        stack = []
        for i in S:
            stack.append(i)
            if len(stack) >= 2:
                if (stack[-1] == ')' and stack[-2] == '('):
                    stack.pop()
                    stack.pop()
                    
        return len(stack)