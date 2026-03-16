class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def backTracking(i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + backTracking(i + 1, j) + backTracking(i - 1, j) + backTracking(i, j + 1) + backTracking(i, j - 1)
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, backTracking(i, j))
        return res