class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        stack = []
        level = 0
        for i in s:
            if i == "(":
                if level != 0:
                    res.append(i)

            if i == "(":
                level += 1
            elif i == ")":
                level -= 1


            if i == ")":
                if level != 0:
                    res.append(i)

        return "".join(res)