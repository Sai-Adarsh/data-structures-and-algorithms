class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backTracking(res, temp, opn, close):
            if len(temp) == 2 * n:
                if temp not in res:
                    res.append(temp)
            if opn < n:
                backTracking(res, temp + "(", opn + 1, close)
            if close < opn:
                backTracking(res, temp + ")", opn, close + 1)

            return res
        return backTracking([], "", 0, 0)