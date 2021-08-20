class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        # Rough
        total = sum(nums)
        
        @cache
        def backTracking(curr_sum, start):
            if start > len(nums):
                return False
            
            if curr_sum > total // 2:
                return False
            
            if start == len(nums):
                return curr_sum == total - curr_sum    
            
            return backTracking(curr_sum + nums[start], start + 1) or backTracking(curr_sum, start + 1)
        
        L = backTracking(0, 0)
        return L