class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        @cache
        def backTracking(m, n):
            
            if m < 0 or n < 0:
                return 0
            
            if m == 0 and n == 0:
                if obstacleGrid[m][n] == 1:
                    return 0
                return 1
            
            if obstacleGrid[m][n] == 1:
                return 0
            
            return backTracking(m - 1, n) + backTracking(m, n - 1)
            
            
        return backTracking(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)