class Solution:
    
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        from sortedcontainers import SortedList
        S = [0]
        for x in nums:
            S.append(S[-1] + x)
            
        P = SortedList(S)
        res = 0
        for x in S:
            P.remove(x)
            i = P.bisect_left(lower + x)
            j = P.bisect_right(upper + x)
            res += max(0, j - i)
        return res