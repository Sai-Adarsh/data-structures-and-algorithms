class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        @cache
        def backTracking(start):
            if start == len(s):
                return True
            
            for i in range(start + 1, len(s) + 1):
                sub_string = s[start : i]
                if sub_string in wordDict:
                    if backTracking(i):
                        return True
                    
            return False
        L = backTracking(0)
        return L