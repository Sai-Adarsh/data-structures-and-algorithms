class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return [list(i) for i in list(permutations(nums))]
