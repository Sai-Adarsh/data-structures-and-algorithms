class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        nums = [i + 1 for i in range(n)]
        return [list(i) for i in combinations(nums, k)]
