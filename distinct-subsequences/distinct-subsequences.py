class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * len(s) for _ in t]
        
		# Check for first row
        final = 0
        for  i in range(len(s)):
            if s[i] == t[0]:
                dp[0][i] = 1
                final += 1
        if not final: return 0 # Just optimization, not essential
        
		# Check for other rows
        for i in  range(1,len(t)):
            left, final = 0, 0
            for j in  range(1, len(s)):
                left += dp[i-1][j-1]
                if s[j] == t[i]:
                    dp[i][j] = left
                    final += left
        return final