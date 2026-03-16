class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        @cache
        def backTracking(i, j):
            if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            neighbors = [(0 , 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in neighbors:
                backTracking(i + dx, j + dy)
            

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    backTracking(i, j)
                    res += 1

        return res