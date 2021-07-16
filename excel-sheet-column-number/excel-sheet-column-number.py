class Solution:
    def titleToNumber(self, s: str) -> int:
        
        s = [i for i in s]
        res = 0
        for i in range(len(s)):
            L = s.pop()
            res += (ord(L) - 64) * (26 ** i)
            
        return res