class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right -= 1
            elif nums[mid] < target:
                left += 1
            else:
                return mid
        return -1