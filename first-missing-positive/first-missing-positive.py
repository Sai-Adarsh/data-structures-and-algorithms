class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        nums = list(set(nums))
        nums.sort()
        left = 0
        right = len(nums) - 1
        target = 1
        while left <= right:
            curr = left + (right - left) // 2
            if target == nums[curr]:
                break
            elif target > nums[curr]:
                left = curr + 1
            else:
                right = curr - 1
        nums[:] = nums[curr:]
        i = 0
        while i < len(nums):
            if nums[i] - 1 != i:
                print(nums[i], i, nums)
                return i + 1
            i += 1
        return i + 1