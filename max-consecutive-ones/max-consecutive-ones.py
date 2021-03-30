class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                temp = 0
            res = max(res, temp)
        return res