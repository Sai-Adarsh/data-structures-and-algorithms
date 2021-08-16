class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        @cache
        def backTracking(i):
            if i >= n:
                if i == n:
                    return 1
                return 0

            res = 0
            poss = [1, 2]
            for each in poss:
                res += backTracking(i + each)

            return res
        L = backTracking(0)
        return L