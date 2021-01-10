class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return
        
        def DFS(board, i, j, word):
            #base case
            if len(word) == 0:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = "#"
            res = DFS(board, i + 1, j, word[1:]) or DFS(board, i - 1, j, word[1:]) or DFS(board, i, j + 1, word[1:]) or DFS(board, i, j - 1, word[1:])
            board[i][j] = temp
            return res
            #recursive case
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if DFS(board, i, j, word) == True:
                    return True
        return False
