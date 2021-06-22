class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        
        
        def DFS(board, i, j):
            q = []
            q.append([i, j])
            
            while q:
                x, y = q.pop(0)
                board[x][y] = "#"
                neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
                for dx, dy in neighbors:
                    if 0 <= x + dx <= len(board) - 1 and 0 <= y + dy <= len(board[0]) - 1 and board[x + dx][y + dy] == "X":
                        q.append([x + dx, y + dy])
        
        
        
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    DFS(board, i, j)
                    res += 1
                    
        return res