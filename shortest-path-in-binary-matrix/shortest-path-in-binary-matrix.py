class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        from collections import deque
        def DFS(grid, i, j):
            #base case
            q = deque([])
            q.append((0, 0, 1))
            visited = set((0, 0))
            
            
            #recursive case
            while q:
                x, y, length = q.popleft()
                if x == len(grid) - 1 and y == len(grid[0]) - 1:
                    return length
                neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
                for nx, ny in neighbours:
                    if 0 <= x + nx <= len(grid) -1 and 0 <= y + ny <= len(grid[0]) - 1 and grid[x + nx][y + ny] == 0 and (x + nx, y + ny) not in visited:
                        visited.add((x + nx, y + ny))
                        q.append((x + nx, y + ny, length + 1))

        
        if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
            return - 1
        to_be_returned = DFS(grid, 0, 0)
        if to_be_returned:
            return to_be_returned
        return -1