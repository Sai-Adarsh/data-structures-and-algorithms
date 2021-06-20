class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = None
        end = None
        for i in range(len(nums) - 1, - 1, -1):
            if nums[i] == target:
                end = i
                break
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
        return [start, end] if (start, end) != (None, None) else [-1, -1]