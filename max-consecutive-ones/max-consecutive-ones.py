class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        res = 0
        for i in nums:
            if i == 0:
                res = max(res, count)
                count = 0
            else:
                count += 1
        res = max(res, count)
        count = 0
        return res