class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        import numpy as np
        dp = np.zeros(shape = (len(text2) + 1, len(text1) + 1))
        
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return int(dp[-1][-1])