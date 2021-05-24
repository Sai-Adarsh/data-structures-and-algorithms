class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        import numpy as np
        dp = np.zeros(shape = (len(word2) + 1, len(word1) + 1))
        
        dp[0][1:] = [_ for _ in range(1, len(dp[0]))]
        for i in range(1, len(dp)):
            dp[i][0] = i
            
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                    
        return int(dp[-1][-1])
                    
        