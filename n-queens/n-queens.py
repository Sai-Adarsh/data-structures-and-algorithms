class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        L = self.backTracking([], [], [], [], n, 0)
        
        return [["".join(['Q' if _ == com else "." for _ in range(n)]) for com in arr] for arr in L]
        
    def backTracking(self, result, queens, diagonal_one, diagonal_two, n, row):
        if row == n:
            result.append(queens)
        
        for col in range(n):
            if col not in queens and row - col not in diagonal_one and row + col not in diagonal_two:
                self.backTracking(result, queens + [col], diagonal_one + [row - col], diagonal_two + [row + col], n, row + 1)
        
        return result