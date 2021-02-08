class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.backtrack([], 0, 0, n, "")
    
    def backtrack(self, sol, opn, close, largest, pair):
        if len(pair) == 2 * largest:
            sol.append(pair)
        if opn < largest:
            self.backtrack(sol, opn+1, close, largest, pair + "(")
        if close < opn:
            self.backtrack(sol, opn, close+1, largest, pair + ")")
        return sol