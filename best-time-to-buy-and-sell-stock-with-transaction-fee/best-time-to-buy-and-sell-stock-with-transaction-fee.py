class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash_profit_summa_irundha, cash_profit_vitha = 0, - prices[0]
        
        i = 0
        
        while i < len(prices):
            cash_profit_summa_irundha = max(cash_profit_summa_irundha, cash_profit_vitha + prices[i] - fee)
            cash_profit_vitha = max(cash_profit_vitha, cash_profit_summa_irundha - prices[i])
            i += 1
        
        return cash_profit_summa_irundha