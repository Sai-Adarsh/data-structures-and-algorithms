class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        @cache
        def backTracking(curr_path, start, count):
            if count == len(nums):
                if curr_path == target:
                    return 1
                return 0
            
            res = 0
            res += backTracking(curr_path + nums[start], start + 1, count + 1) + backTracking(curr_path - nums[start], start + 1, count + 1)
                    
            return res
        
        L = backTracking(0, 0, 0)
        return L