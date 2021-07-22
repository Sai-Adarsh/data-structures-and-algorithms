class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        # generate combinations of indices
        # for each indices, form a new strs, if sorted(min)
        
        if not strs or not strs[0]:
            return 0
        m, n = len(strs), len(strs[0])
        need_compare = set(i for i in range(m - 1))
        delete = 0
        for j in range(n):
            prev_need_compare = set(need_compare)
            for i in prev_need_compare:
                if strs[i][j] > strs[i + 1][j]:
                    need_compare = prev_need_compare
                    delete += 1
                    break
                elif strs[i][j] < strs[i + 1][j]:
                    need_compare.remove(i)
            if not need_compare:
                break
        return delete