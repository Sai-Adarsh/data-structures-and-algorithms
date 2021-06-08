class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        @cache
        def backTracking(s, curr_path):
            if not s:
                return True

            for i in range(1, len(s) + 1):
                substring = s[0: i]
                if substring in wordDict:
                    if backTracking(s[i:], curr_path + substring):
                        return True

            return False

        L = backTracking(s, "")
        return(L)