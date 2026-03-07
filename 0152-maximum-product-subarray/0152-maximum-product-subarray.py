class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum = nums[0]
        minNum = nums[0]
        res = maxNum

        for i in range(1, len(nums)):
            temp = max(maxNum * nums[i], minNum * nums[i], nums[i])
            minNum = min(maxNum * nums[i], minNum * nums[i], nums[i])
            maxNum = temp
            res = max(res, maxNum)

        return res