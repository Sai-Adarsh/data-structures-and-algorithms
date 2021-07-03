class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [1, 2]
        
        for i in range(n - 2):
            dp.append(dp[-1] + dp[-2])
            
        return dp[n - 1]