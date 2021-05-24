class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0, 1]
        
        
        for i in range(n):
            dp.append(dp[-1] + dp[-2])
            
        return dp[-1]