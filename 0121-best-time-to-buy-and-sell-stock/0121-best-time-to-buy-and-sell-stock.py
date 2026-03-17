class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minVal = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - minVal > maxProfit:
                maxProfit = prices[i] - minVal
            if prices[i] < minVal:
                minVal = prices[i]
        return maxProfit