class Solution:
    def totalNQueens(self, n: int) -> int:
        
        L = self.backTracking([], [], [], [], n, 0)
        return len(L)
        
    def backTracking(self, result, queens, diagonal_one, diagonal_two, n, row):
        #base case
        if row == n:
            result.append(queens)
            
        #recursive
        for col in range(n):
            if col not in queens and row - col not in diagonal_one and row + col not in diagonal_two:
                self.backTracking(result, queens + [col], diagonal_one + [row - col], diagonal_two + [row + col], n, row + 1)
        
        return result