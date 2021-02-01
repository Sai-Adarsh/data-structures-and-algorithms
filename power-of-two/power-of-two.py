class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n /= 2
        return n == 1.0