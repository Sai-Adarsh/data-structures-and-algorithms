class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        from itertools import combinations_with_replacement as cp
        L = []
        end = target // min(candidates)
        for i in range(1, end + 1):
            L += list(cp(candidates, i))
        L = list(filter(lambda x: sum(x) == target, L))
        return [list(i) for i in L]
