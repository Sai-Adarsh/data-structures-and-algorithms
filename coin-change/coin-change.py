class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import sys
        @cache
        def backTracking(amount):
            
            if amount < 0:
                return -1
            
            if amount == 0:
                return 0
            
            ans = sys.maxsize
            
            for i in range(len(coins)):
                if backTracking(amount - coins[i]) >= 0:
                    ans = min(ans, backTracking(amount - coins[i]) + 1)
                
            return -1 if ans == sys.maxsize else ans
        return backTracking(amount)