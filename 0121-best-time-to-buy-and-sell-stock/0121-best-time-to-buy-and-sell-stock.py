class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = sys.maxsize
        val = 0

        for i in range(len(prices)):
            val = max(val, prices[i] - minimum)
            minimum = min(minimum, prices[i])

        return val