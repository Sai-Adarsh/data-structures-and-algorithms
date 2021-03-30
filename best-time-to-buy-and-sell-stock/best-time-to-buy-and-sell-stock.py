class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        import sys
        max_profit = 0
        curr_min = sys.maxsize
        
        for i in range(len(prices)):
            if prices[i] > curr_min:
                max_profit = max(max_profit, prices[i] - curr_min)
            curr_min = min(curr_min, prices[i])
            
        return max_profit