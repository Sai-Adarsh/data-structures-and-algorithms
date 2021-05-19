class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        
        ans = prefix = 0 
        seen = [0]
        for x in nums: 
            prefix += x 
            lo = bisect_left(seen, prefix - upper)
            hi = bisect_left(seen, prefix - lower + 1) 
            ans += hi - lo
            insort(seen, prefix)
        return ans 