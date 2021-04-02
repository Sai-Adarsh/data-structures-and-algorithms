class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != ".":
                    if self.isValid(self.board[i][j], i, j) != True:
                        return False
        
        return True
                    
    def isValid(self, num, i, j):
        for row in range(9):
            if self.board[row][j]==num and row!=i:
                print(self.board[row][j],row,j)
                return False
            
        #column check
        for col in range(9):
            if self.board[i][col]==num and col!=j:
                return False
            
        sub_i = (i//3)*3
        sub_j = (j//3)*3
        #checking sub boxes
        for row in range(3):
            for col in range(3):
                if self.board[sub_i+row][sub_j+col]==num and sub_i+row!=i and sub_j+col!=j:
                    return False
        return True