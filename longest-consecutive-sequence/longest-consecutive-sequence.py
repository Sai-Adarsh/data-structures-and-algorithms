class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        
        res = 0
        temp = 1
        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1
                
        res = max(res, temp)
        return res