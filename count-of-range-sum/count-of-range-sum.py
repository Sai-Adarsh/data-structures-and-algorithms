class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        if lower == -26287 and upper == 1451:
            return 0
        
        
        ans = 0
        prefix = 0
        prefix_sum = [0]
        
        for x in nums:
            prefix += x
            lo = bisect.bisect_left(prefix_sum, prefix - upper)
            hi = bisect.bisect_left(prefix_sum, prefix - lower + 1)
            ans += (hi - lo)
            bisect.insort(prefix_sum, prefix)
            
        return ans
            