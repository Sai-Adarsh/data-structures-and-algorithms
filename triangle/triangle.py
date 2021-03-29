class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0 for _ in range(len(triangle) + 1)]
        for row in triangle[::-1]:
            for i, num in enumerate(row):
                dp[i] = num + min(dp[i], dp[i + 1])

        return(dp[0])