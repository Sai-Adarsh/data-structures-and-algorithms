class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
            
        def DFS(board, i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[0] != board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = "#"
            res = DFS(board, i + 1, j, word[1:]) or DFS(board, i - 1, j, word[1:]) or DFS(board, i, j + 1, word[1:]) or DFS(board, i, j - 1, word[1:])
            board[i][j] = temp
            return res
​
​
        res = []
        temp_board = []
        for word in words:
            temp_board[:] = board
            for i in range(len(temp_board)):
                for j in range(len(temp_board[0])):
                    if DFS(temp_board, i, j, word):
                        if word not in res:
                            res.append(word)
        return res
