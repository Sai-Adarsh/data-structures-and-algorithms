class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        def backTracking(d, target):
            if target <= 0 or target > (d * f):
                return 0
            
            if d == 1:
                return 1
            if (d, target) in memo:
                return memo[(d, target)]
            res = 0
            for i in range(1, f + 1):
                res += backTracking(d - 1, target - i)
            memo[(d, target)] = res
            return memo[(d, target)]
        
        memo = {}
        L = backTracking(d, target)
        return L % ((10 ** 9) + 7)