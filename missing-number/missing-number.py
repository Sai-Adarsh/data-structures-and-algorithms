class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        hash_map = {}
        
        for each in nums:
            hash_map[each] = each
        
        for i in range(0, len(nums) + 1):
            if i not in hash_map:
                return i
        
        