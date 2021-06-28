class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        def backTracking(m, n):
            if m < 0 or n < 0 or m > len(board) - 1 or n > len(board[0]) - 1:
                return
            
            if board[m][n] == ".":
                return
            
            board[m][n] = "."
            backTracking(m - 1, n)
            backTracking(m + 1, n)
            backTracking(m, n + 1)
            backTracking(m, n - 1)
        
        
        
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    backTracking(i, j)
                    res += 1
                    
        return res