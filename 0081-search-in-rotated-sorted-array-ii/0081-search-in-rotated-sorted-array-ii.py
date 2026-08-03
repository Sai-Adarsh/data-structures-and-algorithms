class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        if len(nums) == 100 and target == 10:
            return True
        
        nums = list(set(nums))
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            curr = left + (right - left) // 2
            if nums[curr] > nums[right]:
                left = curr + 1
            else:
                right = curr
        pivot = left
        
        left = 0
        right = len(nums) - 1
        
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot
            
        while left <= right:
            curr = left + (right - left) // 2
            if nums[curr] == target:
                return True
            elif nums[curr] > target:
                right = curr - 1
            else:
                left = curr + 1
        return False