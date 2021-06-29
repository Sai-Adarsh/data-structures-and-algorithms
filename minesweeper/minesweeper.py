class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        
        def DFS(x, y):
            q = []
            visited = set()
            q.append([x, y])
            visited.add((x, y))
            
            while q:
                x, y = q.pop(0)
                count = 0
                neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
                for dx, dy in neighbors:
                    if 0 <= x + dx <= len(board) - 1 and 0 <= y + dy <= len(board[0]) - 1 and board[x + dx][y + dy] == "M":
                        count += 1
                        
                if count:
                    board[x][y] = str(count)
                else:
                    board[x][y] = "B"
                    for dx, dy in neighbors:
                        if 0 <= x + dx <= len(board) - 1 and 0 <= y + dy <= len(board[0]) - 1 and (x + dx, y + dy) not in visited and board[x + dx][y + dy] == "E":
                            q.append([x + dx, y + dy])
                            visited.add((x + dx, y + dy))
        
        
        
        
        
        x, y = click
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        else:
            DFS(x, y)
            return board