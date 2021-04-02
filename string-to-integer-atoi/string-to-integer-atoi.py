class Solution:
    def myAtoi(self, s: str) -> int:
        import re
        
        e = re.search(r"^[-+]?\d+", s.lstrip())
        
        e = re.search(r"^[-+]?\d+", s.lstrip())
        return( max(min(int(e.group(0)), 2 ** 31 - 1), -2 ** 31) if e else 0)