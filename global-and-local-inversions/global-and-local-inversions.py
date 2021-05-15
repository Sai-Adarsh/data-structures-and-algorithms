class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        
        
        
        local = 0
        global_ = 0
        
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                local += 1
            if nums[i] < i:
                diff = i - nums[i]
                global_ += diff * (diff + 1) // 2
            
        return local == global_