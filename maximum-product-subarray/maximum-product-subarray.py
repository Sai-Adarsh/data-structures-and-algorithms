class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_pro, min_pro = nums[0], nums[0]
        result = max_pro
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            temp_max = max(curr, max_pro * curr, min_pro * curr)
            min_pro = min(curr, max_pro * curr, min_pro * curr)
            max_pro = temp_max
            result = max(result, max_pro)
            
        return result