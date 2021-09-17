class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        nums = list(set(nums))
        nums.sort()
        
        if not nums:
            return 0
        
        res = 1
        temp = 1
        
        # Naive brute force solution
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1
        
        res = max(res, temp)
        temp = 1
        return res