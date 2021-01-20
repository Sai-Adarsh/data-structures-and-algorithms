class Solution:
    def customSortString(self, S: str, T: str) -> str:
        res = ""
        for i in S:
            if i in T:
                res += T.count(i) * i
        for i in T:
            if i not in S:
                res += i
​
        return res
