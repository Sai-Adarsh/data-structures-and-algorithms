class Solution:
    def beautySum(self, s: str) -> int:
        
        
        L = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
        res = 0
        
        for i in L:
            res += max(Counter(i).values()) - min(Counter(i).values())
            
        return res