class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            max_s, min_s = "ab", "ba"
            val_max, val_min = x, y
        else:
            max_s, min_s = "ba", "ab"
            val_max, val_min = y, x
        res = 0
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= 2:
                if "".join(stack[-2:]) == max_s:
                    res += val_max
                    stack.pop()
                    stack.pop()


        s = "".join(stack)
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= 2:
                if "".join(stack[-2:]) == min_s:
                    res += val_min
                    stack.pop()
                    stack.pop()

        return res