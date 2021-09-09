class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        
        # Stack based problem
        # if # pop.
        # return both stacks are equal
        
        
        def helper(s):
            stack = []
            for i in s:
                stack.append(i)
                if stack:
                    if stack[-1] == "#":
                        if stack:
                            stack.pop()
                        if stack:
                            stack.pop()
            return stack
        
        return helper(s) == helper(t)