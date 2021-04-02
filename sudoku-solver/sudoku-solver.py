class Solution:
    def helper(self, board):
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for num in range(1, 10):
                        num = str(num)
                        if self.isValid(board, i, j, num):
                            board[i][j] = num
                            if self.helper(board):
                                return True
                            board[i][j] = "."
                    return False
        return True
                        
                        
    def isValid(self, board, row, col, num):
        for i in range(9):
            if board[i][col] == num:
                return False
            if board[row][i] == num:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.helper(board)