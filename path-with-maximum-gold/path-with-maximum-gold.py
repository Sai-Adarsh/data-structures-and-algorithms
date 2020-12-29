class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        visited = []
        for i in range(m):
            visited.append([False] * n)
        
        def DFS(i, j, temp):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j] == True:
                return 0
            ans = temp
            visited[i][j] = True
            
            if i + 1 < m:
                ans = max(ans, DFS(i + 1, j, temp + grid[i + 1][j]))
            if i - 1 >= 0:
                ans = max(ans, DFS(i - 1, j, temp + grid[i - 1][j]))
            if j + 1 < n:
                ans = max(ans, DFS(i, j + 1, temp + grid[i][j + 1]))
            if j - 1 >= 0:
                ans = max(ans, DFS(i, j - 1, temp + grid[i][j - 1]))
                
            visited[i][j] = False
            return ans
            
        
        max_length = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_length = max(max_length, DFS(i, j, grid[i][j]))
                    
        
        return max_length
