class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        @cache
        def backTracking(x, y):

            grid[x][y] = "0"
            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in neighbors:
                if 0 <= x + dx <= len(grid) - 1 and 0 <= y + dy <= len(grid[0]) - 1 and grid[x + dx][y + dy] == "1":
                    backTracking(x + dx, y + dy)
 

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    backTracking(i, j)
                    res += 1

        return res