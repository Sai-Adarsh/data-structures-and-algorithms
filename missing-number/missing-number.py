class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        return list(set([i for i in range(len(nums) + 1)]) - set(nums))[-1]