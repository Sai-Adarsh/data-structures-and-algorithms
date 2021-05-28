class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        M = matrix
        if not M or not M[0]: return []
        
        m, n = len(M[0]), len(M)
        def bfs(starts):
            queue = deque(starts)
            visited = set(starts)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]:
                    if 0 <= dx < n and 0 <= dy < m and (dx, dy) not in visited and M[dx][dy] >= M[x][y]:
                        queue.append((dx, dy))
                        visited.add((dx, dy))
                        
            return visited
        
        pacific  = [(0, i) for i in range(m)]   + [(i, 0) for i in range(1,n)]
        atlantic = [(n-1, i) for i in range(m)] + [(i, m-1) for i in range(n-1)]
        
        return bfs(pacific) & bfs(atlantic)