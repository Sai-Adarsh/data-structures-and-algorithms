class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # Optimal dynamic programming approach
        dp = [sys.maxsize for _ in range(len(nums))]
        dp[-1] = 0
        
        for i in range(len(nums) -2, -1, -1):
            dp[i] = 1 + min(dp[i : nums[i] + i + 1]) 
            
        return dp[0]