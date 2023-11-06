class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def backTracking(m, n):
            if m < 0 or n < 0:
                return 0  
            if m == 0 and n == 0:
                return 1
            return backTracking(m - 1, n) + backTracking(m, n - 1)
        
        return backTracking(m - 1, n - 1)