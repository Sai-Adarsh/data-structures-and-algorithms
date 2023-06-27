class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # always maintain min (if bought)
        # 1
        # 0, 0, 4, 4, 5, 5
        currMin = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            currMin = min(currMin, prices[i])
            maxProfit = max(maxProfit, prices[i] - currMin)

        return maxProfit