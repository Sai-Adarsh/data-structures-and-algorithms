class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        L = list(Counter(s).items())
        res = []
        L = sorted(L, key = lambda x: x[1], reverse = True)
        print(L)
        for i in L:
            res += [i[0] * i[1]]
        return "".join(res)
