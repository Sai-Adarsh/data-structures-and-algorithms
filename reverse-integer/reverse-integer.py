class Solution:
    def reverse(self, x: int) -> int:
        
        # Strip
        # slice the neg if neg else don't pic, flag = True based on that
        # reverse and add neg if flag
        
        flag = False
        if x < 0:
            flag = True
        x = str(x)
        if flag:
            x = x[1:]
        x = x[::-1]
        if flag:
            x = "-" + x
        x = int(x)
        return x if (-2 ** 31) <= x <= (2 ** 31) - 1 else 0