class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = nums[0]
        res = maxNum

        for i in range(1, len(nums)):
            # are we starting a fresh array or are we continuing the existing sub array
            maxNum = max(maxNum + nums[i], nums[i])
            # whatever it is, how larget is it compared to the global res
            res = max(res, maxNum)

        return res