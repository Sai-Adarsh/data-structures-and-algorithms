class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        
        def backTracking(m, n, prev_val, matrix, memo):
            if m < 0 or n < 0 or m > len(matrix) - 1 or n > len(matrix[0]) - 1 or prev_val >= matrix[m][n]:
                    return 0
            if (m, n) not in memo:

                memo[(m, n)] =  1 + max(backTracking(m + 1, n, matrix[m][n], matrix, memo), backTracking(m - 1, n, matrix[m][n], matrix, memo), backTracking(m, n + 1, matrix[m][n], matrix, memo), backTracking(m, n - 1, matrix[m][n], matrix, memo))
                return memo[(m, n)]
            else:
                return memo[(m, n)]
        
        
        
        res = 0
        memo = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, backTracking(i, j, matrix[i][j] - 1, matrix, memo))
                
        return res