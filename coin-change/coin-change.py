class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        import sys
        @cache
        def backTracking(amount):

            if amount == 0:
                return 0

            res = sys.maxsize
            for i in range(len(coins)):
                if amount - coins[i] >= 0:
                    res = min(res, backTracking(amount - coins[i]) + 1)
            return res
        L = backTracking(amount)
        return -1 if L == sys.maxsize else L