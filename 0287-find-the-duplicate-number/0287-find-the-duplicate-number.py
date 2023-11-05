class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hashMap = collections.Counter(nums)

        for i, j in hashMap.items():
            if j > 1:
                return i