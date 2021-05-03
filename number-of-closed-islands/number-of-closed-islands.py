class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        
        
        def DFS(grid, i, j):
            # our goal
            # base case
            flag = 0
            q = []
            q.append([i, j])
            
            # our constraints
            # recursive case
            while q:
                x, y = q.pop(0)
                if x in [0, len(grid) - 1] or y in [0, len(grid[0]) - 1]:
                    flag = 1
                grid[x][y] = "#"
                neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
                for dx, dy in neighbours:
                    if 0 <= x + dx <= len(grid) - 1 and 0 <= y + dy <= len(grid[0]) - 1 and grid[x + dx][y + dy] == 0:
                        q.append([x + dx, y + dy])
                        
            return flag
                
        
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    if DFS(grid, i, j) == 0:
                        res += 1
                        
        return res