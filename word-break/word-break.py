class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def backTracking(curr_path, s):
            if not s:
                return True

            for i in range(1, len(s) + 1):
                sub_string = s[0: i]
                if sub_string in wordDict:
                    if backTracking(curr_path + sub_string, s[i : ]):
                        return True

            return False
        L = backTracking("", s)
        return (L)