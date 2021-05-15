class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == sorted(nums, reverse = True):
            nums.sort()
            return nums
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                break
        
        nums[i], nums[j] = nums[j], nums[i]
        nums[:] = nums[:i + 1] + nums[i + 1:][::-1]
        