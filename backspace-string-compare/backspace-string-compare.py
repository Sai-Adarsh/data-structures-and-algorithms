class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stackOps(s):
            stack = []
            for i in s:
                stack.append(i)
                if i == "#":
                    if stack:
                        stack.pop()
                    if stack:
                        stack.pop()
            return stack

        return stackOps(s) == stackOps(t)