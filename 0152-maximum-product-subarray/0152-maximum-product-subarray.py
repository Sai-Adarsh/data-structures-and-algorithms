class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum = nums[0]
        minNum = nums[0]
        res = maxNum

        for i in range(1, len(nums)):
            currNum = nums[i]
            temp = max(maxNum * currNum, minNum * currNum, currNum)
            minNum = min(maxNum * currNum, minNum * currNum, currNum)
            maxNum = temp
            res = max(res, maxNum)

        return res