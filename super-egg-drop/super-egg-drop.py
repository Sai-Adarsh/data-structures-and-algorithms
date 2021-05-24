class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        
        import numpy as np
        dp = np.zeros(shape = (n + 1, k + 1))
        
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i - 1][j]
            if dp[i][j] >= n:
                return i