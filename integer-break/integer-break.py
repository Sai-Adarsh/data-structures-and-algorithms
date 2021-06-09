class Solution:
    def integerBreak(self, n: int) -> int:
        
        
        nums = [i for i in range(1, n)]
        
        @cache
        def backTracking(curr_path, target):
            if target <= 0:
                if target == 0:
                    return curr_path
                return
            
            res = 0
            for i in range(len(nums)):
                if target - nums[i] >= 0:
                    res = max(res, backTracking(curr_path * nums[i], target - nums[i]))
                    
                    
            return res
            
            
            
        L = backTracking(1, n)
        return L