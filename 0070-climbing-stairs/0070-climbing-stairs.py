class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 2]
        for i in range(2, n + 1):
            res += [res[-1] + res[-2]]

        return res[n - 1]