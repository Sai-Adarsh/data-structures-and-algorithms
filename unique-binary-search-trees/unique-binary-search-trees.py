class Solution:
    def numTrees(self, n: int) -> int:
        
        
        catalan_number = factorial(2 * n) // factorial(n) // factorial(n) // (n + 1)
        return catalan_number