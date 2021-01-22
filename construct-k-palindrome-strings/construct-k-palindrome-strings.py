class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        from collections import Counter
        L = list(Counter(s).values())
        odd = 0
        for i in L:
            if i % 2 != 0:
                odd += 1
        print(L)
        return odd <= k
    
