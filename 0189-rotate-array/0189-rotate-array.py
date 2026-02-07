class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - (k % len(nums)):] + nums[:len(nums) - (k % len(nums))]