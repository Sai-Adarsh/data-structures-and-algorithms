class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 
        
        dp = [0]
        i = 1
        while i < len(prices):
            if prices[i - 1] < prices[i]:
                dp.append(dp[-1] + (prices[i] - prices[i - 1]))
            else:
                dp.append(dp[-1])
            i += 1
        return dp[-1]