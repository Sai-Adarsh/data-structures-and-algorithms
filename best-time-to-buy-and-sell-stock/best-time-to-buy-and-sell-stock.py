class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import sys
        i = 0
        max_profit = -prices[0]
        curr_min = sys.maxsize
        while i < len(prices):
            curr_min = min(curr_min, prices[i])
            if prices[i] > curr_min:
                max_profit = max(max_profit, prices[i] - curr_min)
            i += 1
        return max_profit if max_profit != -prices[0] else 0