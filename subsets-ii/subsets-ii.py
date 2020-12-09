class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        L = []
        for i in range(len(nums) + 1):
            L += list(combinations(nums, i))
        L = [tuple(sorted(i)) for i in L]
        L = list(set(L))
        return([list(i) for i in L])
