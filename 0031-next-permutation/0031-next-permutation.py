class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums, sorted(nums, reverse=True))
        if nums == sorted(nums, reverse=True):
            nums.sort()
        else:
            i = len(nums) - 2

            while i > -1:
                if nums[i] < nums[i + 1]:
                    break
                i -= 1

            j = len(nums) - 1

            while j > -1:
                if nums[j] > nums[i]:
                    break
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
            nums[:] = nums[:i + 1] + nums[i + 1:][::-1]