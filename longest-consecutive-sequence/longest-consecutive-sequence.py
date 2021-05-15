class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        
        if len(nums) == 1:
            return 1
        
        res = 0
        count = 0

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        if i == len(nums) - 2 and count >= 1:
            res = max(res, count)
            count = 0
        
        return res + 1