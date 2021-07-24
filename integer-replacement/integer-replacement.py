class Solution:
    def integerReplacement(self, n: int) -> int:
        
        # backTracking approach
        # n % 2 != 0: put poss in backTracking
        # else, put single poss in backTracking
        # n <= 1, if n == 1, return res, cache it
        
        
        @cache
        def backTracking(n, count):
            if n <= 1:
                if n == 1:
                    return count
                return sys.maxsize
            
            
            res = sys.maxsize
            if n % 2 != 0:
                poss = [n - 1, n + 1]
                for each in poss:
                    res = min(res, backTracking(each, count + 1))
            else:
                poss = [n // 2]
                for each in poss:
                    res = min(res, backTracking(each, count + 1))
                    
            return res
        
        L = backTracking(n, 0)
        return L