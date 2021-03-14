class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
    
        
        def DFS(queens, diagonal_one, diagonal_two, row):
            if row == n:
                self.result.append(queens)
            else:
                for col in range(n):
                    if col not in queens and row - col not in diagonal_one and row + col not in diagonal_two:
                        DFS(queens + [col], diagonal_one + [row - col], diagonal_two + [row + col], row + 1)
            
        self.result = []
        DFS([], [], [], 0)
        return [["".join(['Q' if _ == com else "." for _ in range(n)]) for com in arr] for arr in self.result]
    