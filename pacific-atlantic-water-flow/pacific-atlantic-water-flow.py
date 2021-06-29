class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        
        
        def DFS(water):
            q = water
            visited = set(water)
            
            while q:
                x, y = q.pop(0)
                neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
                for dx, dy in neighbors:
                    if 0 <= x + dx <= len(heights) - 1 and 0 <= y + dy <= len(heights[0]) - 1 and heights[x + dx][y + dy] >= heights[x][y] and (x + dx, y + dy) not in visited:
                        q.append([x + dx, y + dy])
                        visited.add((x + dx, y + dy))
        
        
            return visited
        
        pacific = [(0, j) for j in range(len(heights[0]))] + [(i, 0) for i in range(1, len(heights))]
        atlantic = [(len(heights) - 1, j) for j in range(len(heights[0])) ] + [(i, len(heights[0]) - 1) for i in range(len(heights) - 1)]
        one = DFS(pacific)
        two = DFS(atlantic)
        
        return [i for i in one if i in two]