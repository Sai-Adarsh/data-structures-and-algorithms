class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        L = [_ for _ in range(1, 10)]
        
        from itertools import combinations
        L = list(combinations(L, k))
        L = list(filter(lambda x: sum(x) == n, L))
        L = [list(i) for i in L]
        return(L)
