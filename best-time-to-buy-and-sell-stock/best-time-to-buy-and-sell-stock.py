class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        mp = 0
        minimum = prices[0]
        i = 1

        while i < len(prices):
            minimum = min(minimum, prices[i])
            if prices[i] > minimum:
                mp = max(mp, prices[i] - minimum)
            i += 1
        return mp