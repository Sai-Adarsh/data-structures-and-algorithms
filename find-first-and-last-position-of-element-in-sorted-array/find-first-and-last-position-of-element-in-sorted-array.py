class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = -1
        left = bisect.bisect_left(nums, target)
        if 0 <= left <= len(nums) - 1:
            if nums[left] == target:
                left = left
            else:
                left = -1
        else:
            left = -1
        
        right = -1     
        right_high = bisect.bisect_right(nums, target)
        right_low = right_high - 1
        
        if 0 <= right_low <= len(nums) - 1:
            if nums[right_low] == target:
                right = right_low
        
        if 0 <= right_high <= len(nums) - 1:
            if nums[right_high] == target:
                right = right_high
        
        return [left, right]