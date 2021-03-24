class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        L = self.backTracking([], [], [], [], n, 0)
        return [["".join(['Q' if _ == where_queen else "." for _ in range(n)]) for where_queen in arr] for arr in L]
    
    def backTracking(self, res, queens, diagonal_one, diagonal_two, n, row):
        # our goal
        # base case
        if row == n:
            res.append(queens)
            return
        
        # our constraints
        # recursive case
        for col in range(n):
            if col not in queens and row - col not in diagonal_one and row + col not in diagonal_two:
                self.backTracking(res, queens + [col], diagonal_one + [row - col], diagonal_two + [row + col], n, row + 1)
                
        return res
    