class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = nums[0]
        minNum = nums[0]
        res = maxNum

        for i in range(1, len(nums)):
            curr = nums[i]
            temp = max(maxNum + curr, minNum + curr, curr)
            minNum = min(maxNum + curr, minNum + curr, curr)
            maxNum = temp
            res = max(res, maxNum)

        return res