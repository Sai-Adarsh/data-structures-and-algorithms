class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        memo = {}
        def backTracking(m, n):
            if (m, n) in memo:
                return memo[(m, n)]
            if m < 0 or n < 0:
                return 0
            
            if m == 0 and n == 0:
                if obstacleGrid[m][n] == 0:
                    return 1
                return 0
            
            if obstacleGrid[m][n] == 1:
                return 0
            
            memo[(m, n)] = backTracking(m - 1, n) + backTracking(m, n - 1)
            return memo[(m, n)]
        
        L = backTracking(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)
        return L