class Solution:
    def jump(self, nums: List[int]) -> int:
        import sys
        dp = [sys.maxsize for _ in range(len(nums) - 1)] + [0]
        
        for i in range(len(nums) - 2, - 1, - 1):
            try:
                dp[i] = 1 + min(dp[i + 1 : i + nums[i] + 1])
            except:
                dp[i] = sys.maxsize
        return dp[0]