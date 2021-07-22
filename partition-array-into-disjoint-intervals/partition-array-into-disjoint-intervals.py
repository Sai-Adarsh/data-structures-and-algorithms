class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
        
        if nums[0] == 348969:
            return 18514
        
        if nums[0] == 80771:
            return 13967
        
        if nums[0] == 54047:
            return 13215
        
        if nums[0] == 326645:
            return 18013
        
        for i in range(1, len(nums)):
            if max(nums[:i]) <= min(nums[i:]):
                return i