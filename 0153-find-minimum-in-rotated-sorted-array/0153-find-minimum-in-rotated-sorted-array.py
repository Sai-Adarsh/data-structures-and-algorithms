class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] > nums[right]:
                left += 1
            elif nums[left] < nums[right]:
                right -= 1
            
        return nums[right]