class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backTracking(board, i, j, word):
            if not word:
                return True
            if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or board[i][j] != word[0]:
                return False
            temp = board[i][j]
            board[i][j] = "#"
            res = backTracking(board, i + 1, j, word[1:]) or backTracking(board, i - 1, j, word[1:]) or backTracking(board, i, j + 1, word[1:]) or backTracking(board, i, j - 1, word[1:])
            board[i][j] = temp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backTracking(board, i, j, word):
                        return True
        return False