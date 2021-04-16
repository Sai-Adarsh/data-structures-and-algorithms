class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stackOps(s):
            i = 0
            stack = []
            while i < len(s):
                if s[i] == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(s[i])
                i += 1
            return stack

        return stackOps(s) == stackOps(t)