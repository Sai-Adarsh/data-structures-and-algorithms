class Solution:
    def mySqrt(self, x: int) -> int:
        
        # Newton's square root approximation method
        if x == 0:
            return 0
        
        approx = 0.5 * x
        
        for i in range(20):
            betterApprox = 0.5 * (approx + (x / approx))
            approx = betterApprox
        
        return math.floor(approx)