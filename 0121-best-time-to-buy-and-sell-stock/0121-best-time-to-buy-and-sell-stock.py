class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - minimum > profit:
                profit = prices[i] - minimum
            if prices[i] < minimum:
                minimum = prices[i]

        return profit