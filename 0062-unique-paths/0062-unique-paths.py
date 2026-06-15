class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def backTracking(x, y):
            if x == 0 and y == 0:
                return 1
            if x < 0 or x >= m or y < 0 or y >= n:
                return 0

            return backTracking(x - 1, y) + backTracking(x, y - 1)

        return backTracking(m - 1, n - 1)