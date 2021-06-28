class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def DFS(board, i, j):
            q = []
            q.append([i, j])
            
            while q:
                x, y = q.pop()
                board[x][y] = "*"
                neighbors = ((0, 1), (0, -1), (1, 0), (-1, 0))
                for dx, dy in neighbors:
                    if 0 <= x + dx <= len(board) - 1 and 0 <= y + dy <= len(board[0]) - 1 and board[x + dx][y + dy] == "O":
                        q.append([x + dx, y + dy])
                        
        
        # first row
        i = 0
        for j in range(len(board[0])):
            if board[i][j] == "O":
                DFS(board, i, j)
                
        # last row
        i = len(board) - 1
        for j in range(len(board[0])):
            if board[i][j] == "O":
                DFS(board, i, j)
                
        # first column
        j = 0
        for i in range(len(board)):
            if board[i][j] == "O":
                DFS(board, i, j)
                
        # last column
        j = len(board[0]) - 1
        for i in range(len(board)):
            if board[i][j] == "O":
                DFS(board, i, j)
                
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "*":
                    board[i][j] = "O"