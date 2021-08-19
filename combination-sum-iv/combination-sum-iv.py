class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        @cache
        def backTracking(target):
            if not target:
                return 1
            
            res = 0
            for i in range(len(nums)):
                if target - nums[i] >= 0:
                    res += backTracking(target - nums[i])
            
            return res
        
        L = backTracking(target)
        return L