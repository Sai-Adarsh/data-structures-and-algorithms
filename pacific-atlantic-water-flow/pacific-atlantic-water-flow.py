class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        
        
        
        def DFS(water):
            q = water
            visited = set(water)
            
            while q:
                x, y = q.pop(0)
                neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
                for dx, dy in neighbors:
                    if 0 <= x + dx <= len(matrix) - 1 and 0 <= y + dy <= len(matrix[0]) - 1 and (x + dx, y + dy) not in visited and matrix[x + dx][y + dy] >= matrix[x][y]:
                        q.append([x + dx, y + dy])
                        visited.add((x + dx, y + dy))
                        
            return visited
        
        
        pacific = [(0, j) for j in range(len(matrix[0]))] + [(i, 0) for i in range(1, len(matrix))]
        atlantic = [(len(matrix) - 1, j) for j in range(len(matrix[0]) - 1, - 1, - 1) ] + [(i, len(matrix[0]) - 1) for i in range(len(matrix) - 1)]
        
        one = DFS(pacific)
        two = DFS(atlantic)
        
        L = [i for i in one if i in two]
        return L