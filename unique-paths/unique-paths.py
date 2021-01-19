class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import numpy
        dp = numpy.ones(shape = (m, n))
        #print(dp)
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return int(dp[-1][-1])
