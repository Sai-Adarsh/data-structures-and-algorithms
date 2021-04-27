class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        
        S = [0]
        for i in nums:
            S.append(S[-1] + i)
        
        P = sorted(S)
        res = 0
        
        for x in S:
            P.remove(x)
            i = bisect.bisect_left(P, lower + x)
            j = bisect.bisect_right(P, upper + x)
            res += max(0, j - i)
            
        return res
            