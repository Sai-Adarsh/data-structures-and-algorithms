class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        L = self.backTracking([], [], [], [], 0, n)
        return [["".join(['Q' if _ == queen_at else '.' for _ in range(n)]) for queen_at in arr] for arr in L]
        
    def backTracking(self, res, queen, diagonal_one, diagonal_two, row, n):
        # our goal
        # base case
        if row == n:
            res.append(queen)
        
        # our constraint
        for col in range(n):
            if col not in queen and row - col not in diagonal_one and row + col not in diagonal_two:
                # our choice
                self.backTracking(res, queen + [col], diagonal_one + [row - col], diagonal_two + [row + col], row + 1, n)
        
        return res
        
        