class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        if n >= 1:
            return math.log10(n) / math.log10(4) % 1 == 0
        else:
            return False