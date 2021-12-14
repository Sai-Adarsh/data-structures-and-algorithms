class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        
        def backTracking(target):
            if target in memo:
                return memo[target]
            if target <= 0:
                if target == 0:
                    return 0
                return - 1
            
            res = sys.maxsize
            for i in range(len(coins)):
                if target - coins[i] >= 0:
                    res = min(res, backTracking(target - coins[i]) + 1)
                    
            memo[target] = res
            return memo[target]
        L = backTracking(amount)
        return L if L != sys.maxsize else -1