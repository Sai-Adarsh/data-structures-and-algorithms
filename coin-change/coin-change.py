class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        import sys
        import numpy as np
        
        dp = np.zeros(shape = (len(coins) + 1, amount + 1))
        
        dp[0] = [sys.maxsize for _ in range(len(dp[0]))]
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if j >= coins[i - 1]:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - coins[i - 1]])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return int(dp[-1][-1]) if dp[-1][-1] != sys.maxsize else -1