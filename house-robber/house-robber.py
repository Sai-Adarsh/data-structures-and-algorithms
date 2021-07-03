class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[-1]
        
        
        dp = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            dp.append(max(dp[-1], nums[i] + dp[-2]))
            
        return dp[-1]