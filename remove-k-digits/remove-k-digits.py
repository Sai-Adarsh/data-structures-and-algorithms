class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
​
        i = 0
        while i < len(num):
            while k and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        while k:
            stack.pop()
            k -= 1
        return("".join(stack).lstrip('0') or '0')
