class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or sorted(prices, reverse = True) == prices:
            return 0
        dp = [0 for _ in range(len(prices))]
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                dp[i] += dp[i - 1] + (prices[i] - prices[i - 1])
            else:
                dp[i] = dp[i - 1]
        return dp[-1]