class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        from itertools import product
​
        L = list(map(''.join, product(*zip(S.lower(), S.upper()))))
        return list(set(L))
