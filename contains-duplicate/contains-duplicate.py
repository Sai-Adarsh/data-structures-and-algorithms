class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        hash_set = {}
        
        for i in nums:
            if i not in hash_set:
                hash_set[i] = i
            else:
                return True
            
        return False