class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashMap = {}
        res = []

        for eachNum in nums:
            hashMap[eachNum] = eachNum

        
        for ind in range(len(nums) + 1):
            if ind not in hashMap:
                return ind