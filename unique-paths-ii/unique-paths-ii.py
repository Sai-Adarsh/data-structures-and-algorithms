class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        
        for j in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1:
                obstacleGrid[0][j] = 1
            else:
                obstacleGrid[0][j] = 0
                
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = 0
                
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                    
        return obstacleGrid[-1][-1]