class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(('(', i))
            elif s[i] == ')':
                stack.append((')', i))
                if len(stack) > 1:
                    if stack[-1][0] == ')' and stack[-2][0] == '(':
                        stack.pop()
                        stack.pop()
        s = [i for i in s]
        for x in stack:
            s[x[1]] = None
        return("".join([i for i in s if i != None]))