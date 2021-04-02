class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        import sys
        dp = [[sys.maxsize - 10000 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                        
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if i < len(matrix) - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j < len(matrix[0]) - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
                    
        return dp