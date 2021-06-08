class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
    
        cache = {}
        
        def backTracking(nums, curr_index, target):
            if (curr_index, target) in cache:
                return cache[(curr_index, target)]
            
            if curr_index == 0:
                if target == 0:
                    return 1
                else:
                    return 0
            else:
                cache[(curr_index, target)] =  backTracking(nums, curr_index - 1, target - nums[curr_index - 1]) + backTracking(nums, curr_index - 1, target + nums[curr_index - 1])
                return cache[(curr_index, target)]
            
            
                
                
        
        return backTracking(nums, len(nums), target)
                