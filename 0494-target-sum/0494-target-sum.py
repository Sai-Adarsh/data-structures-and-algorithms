class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def backTracking(index, currVal):
            if index == len(nums):
                if currVal == target:
                    return 1
                else:
                    return 0

            plus = backTracking(index + 1, currVal + nums[index]) 
            minus = backTracking(index + 1, currVal - nums[index]) 
            return plus + minus
        
        return backTracking(0, 0)
