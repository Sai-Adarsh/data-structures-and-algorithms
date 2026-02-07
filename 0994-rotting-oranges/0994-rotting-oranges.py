class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j])

        res = 0
        while q:
            isDone = False
            for i in range(len(q)):
                x, y = q.pop(0)
                neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dx, dy in neighbors:
                    if 0 <= x + dx <= len(grid) - 1 and 0 <= y + dy <= len(grid[0]) - 1 and grid[x + dx][y + dy] == 1 and (x + dx, y + dy) not in visited:
                        grid[x + dx][y + dy] = 2
                        q.append([x + dx, y + dy])
                        visited.add((x + dx, y + dy))
                        isDone = True
            if isDone:
                res += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return res