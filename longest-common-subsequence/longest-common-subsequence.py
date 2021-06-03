class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def backTracking(m, n):
            if m < 0 or n < 0:
                return 0
            
            return 1 + backTracking(m - 1, n - 1) if text2[m] == text1[n] else max(backTracking(m - 1, n), backTracking(m, n - 1))
        
        
        return backTracking(len(text2) - 1, len(text1) - 1)