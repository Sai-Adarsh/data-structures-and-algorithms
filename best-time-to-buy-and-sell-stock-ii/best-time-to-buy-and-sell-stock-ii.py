class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]
        i = 1

        while i < len(prices):
            if prices[i - 1] < prices[i]:
                dp.append(dp[-1] + (prices[i] - prices[i - 1]))
            i += 1
        return dp[-1]