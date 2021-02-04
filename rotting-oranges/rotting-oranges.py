class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        time_required = 0
        q = deque()
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    
        while q:
            operation_done = False
            for _ in range(len(q)):
                x, y = q.popleft()
                neighbour = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                for i, j in neighbour:
                    if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) and grid[i][j] == 1:
                        operation_done = True
                        q.append((i, j))
                        grid[i][j] = 2
            if operation_done == True:
                time_required += 1
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                    
        return time_required