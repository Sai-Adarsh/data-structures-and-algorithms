class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()


        res = 0
        count = 0
        i = 0
        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                res = max(res, count)
                count = 0
            else:
                count += 1

        if i == len(nums) - 2:
            res = max(res, count)
            count = 0

        return (res + 1)