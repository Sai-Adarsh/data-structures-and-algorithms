class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        # [s, s, s, s, 0]
        #      ,1 ,1 ,0
    
            
        dp = [sys.maxsize for _ in range(len(nums))]
        dp[-1] = 0
        
        for i in range(len(nums) - 2, -1, -1):
            dp[i] = 1 + min(dp[i: i + nums[i] + 1])
            
        return dp[0]