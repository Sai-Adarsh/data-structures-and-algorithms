class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prevVal = 1
        nextVal = 2
 
        for i in range(2, n):
            temp = nextVal
            nextVal += prevVal
            prevVal = temp
        
        return nextVal