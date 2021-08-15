class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # set(actuals) - set(nums)
        return list(set([_ for _ in range(len(nums) + 1)]) - set(nums))[0]