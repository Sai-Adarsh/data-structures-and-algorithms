class Solution:
    def isValid(self, s: str) -> bool:
        
        
        stack = []
        
        for i in s:
            stack.append(i)
            if len(stack) >= 2:
                if (stack[-1] == ")" and stack[-2] == "(") or (stack[-1] == "]" and stack[-2] == "[") or (stack[-1] == "}" and stack[-2] == "{"):
                    stack.pop()
                    stack.pop()
                    
                    
        return not stack
                    