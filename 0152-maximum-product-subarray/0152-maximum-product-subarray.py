class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        res = maxProd

        for i in range(1, len(nums)):
            curr = nums[i]
            temp = max(maxProd * curr, minProd * curr, curr)
            minProd = min(maxProd * curr, minProd * curr, curr)
            maxProd = temp
            res = max(res, maxProd)

        return res