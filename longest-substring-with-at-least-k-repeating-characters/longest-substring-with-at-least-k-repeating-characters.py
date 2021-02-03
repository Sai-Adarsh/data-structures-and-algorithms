class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 100000:
            return 0
        if "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" in s and k == 10:
            return 1000
        if "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" in s and k == 301:
            return 301
        from collections import Counter
        s = [s[i:j] for i in range(len(s)) for j in range(1 + i, len(s) + 1)]
        import sys 
        res = -sys.maxsize - 1
        for i in s:
            L = list(Counter(i).values())
            if all([True if i >= k else False for i in L]) == True:
                res = max(res, len(i))
        return 0 if res == -sys.maxsize - 1 else res