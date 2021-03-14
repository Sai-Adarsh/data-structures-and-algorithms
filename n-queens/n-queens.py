class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        
        def DFS(queens, d1_diff, d2_diff):
            row = len(queens)
            
            if row == n:
                result.append(queens)
            else:
                for col in range(n):
                    if col not in queens and row - col not in d1_diff and row + col not in d2_diff:
                        DFS(queens + [col], d1_diff + [row - col], d2_diff + [row + col])
            
        result = []
        DFS([], [], [])
        
        return [["".join(['Q' if _ ==  com else '.' for _ in range(n) ]) for com in arr] for arr in result]