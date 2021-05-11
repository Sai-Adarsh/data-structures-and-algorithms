class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        import math
        if num > 0:
            return math.log10(num) / math.log10(4) % 1 == 0
        else:
            return 0