class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxNum = nums[0]
        minNum = nums[0]
        res = maxNum

        for i in range(1, len(nums)):
            curr = nums[i]
            temp = max(curr, maxNum * curr, minNum * curr)
            minNum = min(curr, maxNum * curr, minNum * curr)
            maxNum = temp
            res = max(res, maxNum)

        return res