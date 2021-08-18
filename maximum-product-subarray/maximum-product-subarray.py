class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_num = nums[0]
        min_num = nums[0]
        
        res = max_num
        
        for i in range(1, len(nums)):
            
            curr_num = nums[i]
            
            temp = max(curr_num, curr_num * max_num, curr_num * min_num)
            min_num = min(curr_num, curr_num * max_num, curr_num * min_num)
            max_num = temp
            res = max(res, max_num)
            
        return res