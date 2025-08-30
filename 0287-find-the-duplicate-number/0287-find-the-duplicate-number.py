class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hashMap = collections.Counter()

        for each in nums:
            if hashMap[each] == 1:
                return each
            hashMap[each] += 1