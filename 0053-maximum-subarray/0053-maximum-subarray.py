class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = nums[0]
        res = maxNum

        for i in range(1, len(nums)):
            maxNum = max(maxNum + nums[i], nums[i])
            res = max(res, maxNum)

        return res