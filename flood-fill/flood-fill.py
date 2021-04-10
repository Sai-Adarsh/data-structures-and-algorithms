class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        
        def DFS(image, i, j, newColor, currColor):
            # our solution
            # base case
            q = []
            q.append([i, j])
            visited = set()
            visited.add((i, j))
            
            # our constraints
            # recursive case
            while q:
                x, y = q.pop()
                image[x][y] = newColor
                neighbours = ((1, 0), (-1, 0), (0, 1), (0, -1))
                for dx, dy in neighbours:
                    if 0 <= x + dx <= len(image) - 1 and 0 <= y + dy <= len(image[0]) - 1 and image[x + dx][y + dy] == currColor and tuple((x + dx, y + dy)) not in visited:
                        
                        visited.add(tuple((x + dx, y + dy)))
                        q.append([x + dx, y + dy])
            return image
        
        for i in range(len(image)):
            for j in range(len(image[0])):
                if i == sr and j == sc:
                    return DFS(image, i, j, newColor, image[sr][sc])