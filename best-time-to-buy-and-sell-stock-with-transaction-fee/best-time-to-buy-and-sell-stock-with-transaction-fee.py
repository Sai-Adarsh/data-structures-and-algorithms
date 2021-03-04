class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = - prices[0]
        
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash