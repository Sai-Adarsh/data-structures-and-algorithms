class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        hashMap = {}

        for eachNum in nums:
            hashMap[eachNum] = 1

        arr = []
        for eachNum in range(1, len(nums) + 1):
            if eachNum not in hashMap:
                arr.append(eachNum)
        
        return arr