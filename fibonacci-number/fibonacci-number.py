class Solution:
    def fib(self, n: int) -> int:
        
        
        # tabulation DP
        fibo = [0, 1]
        
        for i in range(n - 2 + 1):
            fibo.append(fibo[-1] + fibo[-2])
        
        return fibo[n]