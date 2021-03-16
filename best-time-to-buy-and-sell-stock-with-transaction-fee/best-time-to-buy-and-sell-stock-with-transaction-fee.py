class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = 0, - prices[0]
        
        i = 1
        while i < len(prices):
            buy = max(buy, sell + prices[i] - fee)
            sell = max(sell, buy - prices[i])
            i += 1
        return buy