class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n=len(s)
        if not n:
            return 0
        if s[::-1]==s:
            return 1
        else:
            return 2