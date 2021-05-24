class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        @cache
        def backTracking(m, n):
            if m < 0 or n < 0:
                return sys.maxsize
            
            if m == 0 and n == 0:
                return grid[0][0]
            
            
            return grid[m][n] + min(backTracking(m - 1, n), backTracking(m, n - 1))
            
            
        return backTracking(len(grid) - 1, len(grid[0]) - 1)