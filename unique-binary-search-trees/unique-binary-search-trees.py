class Solution:
    def numTrees(self, n: int) -> int:
        return factorial(2 * n) // factorial(n) // factorial(n) // (n+1)