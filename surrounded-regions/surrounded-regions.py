class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0]) if m > 0 else 0 
            
        def DFS(i, j):                              
            if board[i][j] == "O":
                board[i][j] = 'D'
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < m and 0 <= y < n:
                        DFS(x,y)
                            
        for i in range(m):
            DFS(i, 0)
            DFS(i, n-1)
        
        for i in range(n):
            DFS(0, i)
            DFS(m-1, i)
            
        for i in range(m):
            for j in range(n):
                if board[i][j]== 'D' :
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"