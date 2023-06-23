class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache
        def backTracking(start):
            if start == len(s):
                return True
            
            for i in range(start + 1, len(s) + 1):
                subString = s[start : i]
                if subString in wordDict:
                    if backTracking(i):
                        return True

        return backTracking(0)