class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        fibo = [1, 2]
        
        for i in range(n - 2):
            fibo.append(fibo[-1] + fibo[-2])
            
        return fibo[n - 1]