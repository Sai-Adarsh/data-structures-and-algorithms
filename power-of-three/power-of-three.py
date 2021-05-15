class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        import math
        if n >= 1:
            return math.log10(n) / math.log10(3) % 1 == 0
        else:
            return False