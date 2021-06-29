class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        @cache
        def backTracking(m, n, prev_val):
            if m < 0 or n < 0 or m > len(matrix) - 1 or n > len(matrix[0]) - 1 or prev_val >= matrix[m][n]:
                    return 0
                
            return 1 + max(backTracking(m + 1, n, matrix[m][n]), backTracking(m - 1, n, matrix[m][n]), backTracking(m, n + 1, matrix[m][n]), backTracking(m, n - 1, matrix[m][n]))
        
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, backTracking(i, j, matrix[i][j] - 1))
                
        return res