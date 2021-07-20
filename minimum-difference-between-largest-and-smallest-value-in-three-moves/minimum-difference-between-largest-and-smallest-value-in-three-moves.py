class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) < 5:
            return 0
        n = len(nums) 
        res = sys.maxsize
        nums.sort()
        for x in range(4):
            res = min (res, nums[n - 4 + x] - nums[x])
        return res