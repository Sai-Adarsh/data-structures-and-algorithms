class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        from math import floor
        approx = 0.5 * x
        
        for _ in range(20):
            better_approx = 0.5 * (approx + (x / approx))
            approx = better_approx
            
        return floor(better_approx)