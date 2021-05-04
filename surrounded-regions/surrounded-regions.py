class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def DFS(board, i, j):
            board[i][j] = "*"
            neighbours = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for dx, dy in neighbours:
                if 0 <= i + dx <= len(board) - 1 and 0 <= j + dy <= len(board[0]) - 1 and board[i + dx][j + dy] == "O":
                    DFS(board, i + dx, j + dy)
        
        
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
                
        # left column
        j = 0
        for i in range(len(board)):
            if board[i][j] == "O":
                DFS(board, i, j)
                
        # right column
        j = len(board[0]) - 1
        for i in range(len(board)):
            if board[i][j] == "O":
                DFS(board, i, j)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "*":
                    board[i][j] = "O"
                    