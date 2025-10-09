class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # note down minimum
        # val = max(val, curr - minimum)
        # min = min(min, curr)
        # 7, 1, 5, 3, 6, 4
        # 7, 1, 5, 3, 6, 4
        # 0, 1, 4, 4, 5, 5
        minimum = sys.maxsize
        val = 0

        for i in range(len(prices)):
            val = max(val, prices[i] - minimum)
            minimum = min(minimum, prices[i])

        return val