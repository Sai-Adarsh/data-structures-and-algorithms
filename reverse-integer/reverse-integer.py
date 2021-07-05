class Solution:
    def reverse(self, x: int) -> int:
        
        neg_in = False
        x = str(x)[::-1]
        
        if "-" in x:
            x = x[:-1]
            x = "-" + x
        return int(x) if -(2 ** 31) <= int(x) <= (2 ** 31) - 1 else 0