class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            curr = left + (right - left) // 2
            if nums[curr] > target:
                right = curr - 1
            elif nums[curr] < target:
                left = curr + 1
            else:
                return curr
        return -1