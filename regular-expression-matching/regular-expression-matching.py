class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = '^' + p + '$'
        import re
        regexp = re.compile(p)
        if re.match(p,s):
            return True
        else:
            return False
            