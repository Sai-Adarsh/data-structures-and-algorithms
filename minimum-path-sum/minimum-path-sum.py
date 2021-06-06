class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        memo = defaultdict(tuple)
        def backTracking(m, n):
            if not memo[(m, n)]:
                if m == 0 and n == 0:
                    return grid[0][0]

                if m < 0 or n < 0:
                    return sys.maxsize

                memo[(m, n)] = grid[m][n] + min(backTracking(m - 1, n), backTracking(m, n - 1))
                return memo[(m, n)]
            else:
                return memo[(m, n)]
        
            
        return backTracking(len(grid) - 1, len(grid[0]) - 1)