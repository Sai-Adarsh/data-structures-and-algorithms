class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        j = 0
        i = j + 1
        dp = [1 for i in range(len(nums))]
        while i < len(nums):
            while j < i:
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])           
                j += 1
            j = 0
            i += 1
        return max(dp)
