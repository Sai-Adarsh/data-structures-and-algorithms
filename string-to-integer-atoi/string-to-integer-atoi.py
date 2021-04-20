class Solution:
    def myAtoi(self, s: str) -> int:
        import re
        
        e = re.search("^[-+]?\d+", s.lstrip())
        L = (int(e.group()) if e else 0)
        if L > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if L < -2 ** 31:
            return -2 ** 31
        
        return L if L else 0