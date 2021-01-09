class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        
        def DFS(grid, i, j):
            self.curr_area += 1
            grid[i][j] = "#"
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                DFS(grid, i + 1, j)
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                DFS(grid, i - 1, j)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                DFS(grid, i, j + 1)
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                DFS(grid, i, j - 1)
​
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.curr_area = 0
                    DFS(grid, i, j)
                    max_area = max(max_area, self.curr_area)
        return max_area
