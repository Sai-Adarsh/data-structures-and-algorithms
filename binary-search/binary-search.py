class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            curr = left + (right - left) // 2
            if nums[curr] == target:
                return curr
            elif target > nums[curr]:
                left = curr + 1
            else:
                right = curr - 1
        return -1
