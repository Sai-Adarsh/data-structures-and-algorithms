class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        total = sum(nums)
        @cache
        def backTracking(i, curr_sum):
            if curr_sum > total // 2:
                return False
            
            if i < 0:
                return curr_sum == total - curr_sum
            
            return backTracking(i - 1, curr_sum + nums[i]) or backTracking(i - 1, curr_sum)
            
            
        return backTracking(len(nums) - 1, 0)