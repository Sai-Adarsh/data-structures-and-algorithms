class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        hashMap = {}

        for i in nums:
            hashMap[i] = 1

        arr = []
        for i in range(1, len(nums) + 1):
            if i not in hashMap:
                arr.append(i)
        
        return arr
