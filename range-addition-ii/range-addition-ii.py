class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        
        c, d = ops[0][0], ops[0][1]
        for i in ops:
            c = min(c, i[0])
            d = min(d, i[1])
        return c * d