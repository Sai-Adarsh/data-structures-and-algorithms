class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        memo = {}
        def backTracking(target, start):
            if (target, start) in memo:
                return memo[(target, start)]
            if start == len(nums):
                if target <= 0:
                    if target == 0:
                        return 1
                return 0
            
            res = 0
            res = backTracking(target - nums[start], start + 1) + backTracking(target + nums[start], start + 1)
            memo[(target, start)] = res
            return memo[(target, start)]
        
        L = backTracking(target, 0)
        return L