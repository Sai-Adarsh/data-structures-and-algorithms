class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            a, b = 1, 2
            for i in range(2, n):
                res = a + b
                a = b
                b = res

            return res