class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return True