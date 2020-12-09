class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        L = []
        for i in range(len(nums) + 1):
            L += list(combinations(nums, i))
        return ([list(i) for i in L])
