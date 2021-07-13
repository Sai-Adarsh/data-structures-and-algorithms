class Solution:
    def minOperations(self, n: int) -> int:
        h = n // 2
        # odd 
        if n % 2 == 0:
            return h * (n - h)
        return h * (h + 1)