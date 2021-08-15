class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        
        # set(actuals) - set(nums)
        return list(set([_ for _ in range(1, len(nums) + 1)]) - set(nums))