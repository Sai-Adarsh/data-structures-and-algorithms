class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hash_set = {}
        for i in nums:
            if i not in hash_set:
                hash_set[i] = i
            else:
                return i
        
