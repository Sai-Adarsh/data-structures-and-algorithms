class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or sorted(prices, reverse = True) == prices:
            return 0
        
        max_profit = 0
        curr_min = prices[0]
        
        for i in range(1, len(prices)):
            curr_min = min(curr_min, prices[i])
            if prices[i] > curr_min:
                max_profit = max(max_profit, prices[i] - curr_min)
        return max_profit