class Solution:
    def integerBreak(self, n: int) -> int:
        
        
        nums = [i for i in range(1, n)]
        
        memo = {}
        def backTracking(curr_path, target):
            if (curr_path, target) not in memo:
                if target <= 0:
                    if target == 0:
                        return curr_path
                    return 0

                res = 0
                for i in range(len(nums)):
                    if target - nums[i] >= 0:
                        res = max(res, backTracking(curr_path * nums[i], target - nums[i]))

                memo[(curr_path, target)] = res
                return memo[(curr_path, target)]
            else:
                return memo[(curr_path, target)]
            
            
        L = backTracking(1, n)
        return L