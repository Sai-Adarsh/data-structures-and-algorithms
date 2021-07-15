class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                is_there = bisect.bisect_left(nums, nums[i] + nums[j])
                res += max(0, is_there - j - 1)
                
        return res