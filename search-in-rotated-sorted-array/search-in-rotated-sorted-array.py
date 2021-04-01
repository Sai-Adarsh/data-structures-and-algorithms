class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            curr = left + (right - left) // 2
            if nums[curr] > nums[right]:
                left = curr + 1
            else:
                right = curr
                
        start = left
        left = 0
        right = len(nums) - 1
        
        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start
            
        while left <= right:
            curr = left + (right - left) // 2
            if target == nums[curr]:
                return curr
            elif nums[curr] > target:
                right = curr - 1
            else:
                left = curr + 1
        return -1