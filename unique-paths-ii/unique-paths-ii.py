class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        m = 0
        n = 0

        @functools.lru_cache(None)
        def backTracking(m, n):
            if m == len(obstacleGrid) - 1 and n == len(obstacleGrid[0]) - 1 and obstacleGrid[m][n] == 0:
                return 1
            
            if m > len(obstacleGrid) - 1 or n > len(obstacleGrid[0]) - 1:
                return 0
            
            if obstacleGrid[m][n] == 1:
                return 0
            
            res = 0
            res += backTracking(m + 1, n)
            res += backTracking(m, n + 1)
            return res
        
        return backTracking(0, 0)
            