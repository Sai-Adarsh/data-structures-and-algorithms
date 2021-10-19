class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        
        one, two = 0, 0
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                one += 1
            elif nums[i] > nums[i + 1]:
                two += 1
                
                
        if (one and not two) or (not one and two):
            return True
        if not one and not two:
            return True
        else:
            return False