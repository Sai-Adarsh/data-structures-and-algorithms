class Solution:
    def isValid(self, s: str) -> bool:
        
        hashMap = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = []
        for eachChar in s:
            stack.append(eachChar)
            if len(stack) >= 2:
                if stack[-2] in hashMap:
                    if stack[-1] ==  hashMap[stack[-2]]:
                        for lIter in range(2):
                            stack.pop()

        return not stack