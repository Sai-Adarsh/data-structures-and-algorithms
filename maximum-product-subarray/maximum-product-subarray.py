class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxNum = nums[0]
        minNum = nums[0]
        res = maxNum
        
        for i in range(1, len(nums)):
            currProd = nums[i]
            temp = max(currProd, maxNum * currProd, minNum * currProd)
            minNum = min(currProd, maxNum * currProd, minNum * currProd)
            maxNum = temp
            res = max(res, maxNum)
            
        return res