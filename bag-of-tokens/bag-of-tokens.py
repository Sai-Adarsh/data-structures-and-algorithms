class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        
        tokens.sort()
        
        res = 0
        ans = 0
        
        while True:
            if not tokens:
                break
            if P >= tokens[0]:
                P -= tokens.pop(0)
                res += 1
                ans = max(res, ans)
            elif res >= 1:
                P += tokens.pop()
                res -= 1
            else:
                break
        return ans