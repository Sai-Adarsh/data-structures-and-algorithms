class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return
        if len(nums) <= 2:
            return max(nums)
        dp = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            dp.append(max(dp[-1], dp[-2] + nums[i]))
        return dp[-1]