class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        if not scores or not ages:
            return 0
        n = len(scores)
        info = sorted(zip(ages, scores))
        dp = [0] * n
        for i in range(n):
            dp[i] = info[i][1]
            for j in range(i):
                if info[j][1] <= info[i][1]:
                    dp[i] = max(dp[i], dp[j] + info[i][1])
        return max(dp)