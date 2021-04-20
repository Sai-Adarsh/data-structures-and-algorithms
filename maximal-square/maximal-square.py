class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        @cache
        def backTracking(i, j, n, m):
            # our goal
            # base case
            if i == 0 or j == 0:
                return int(matrix[i][j])
            
            if matrix[i][j] == "0":
                return 0
            
            return min(backTracking(i - 1, j - 1, n, m), backTracking(i - 1, j, n, m), backTracking(i, j - 1, n, m)) + 1
        
        
        ans = 0
        
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                ans = max(ans, backTracking(i, j, n, m))
            
        return ans * ans