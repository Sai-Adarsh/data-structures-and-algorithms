class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashMap = {}
        for eachNum in nums:
            hashMap[eachNum] = eachNum

        for i in range(1, len(nums) + 1):
            if i not in hashMap:
                return i

        return i + 1