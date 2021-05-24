class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        count = 0
        L = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
        for i in L:
            if i == i[::-1]:
                count += 1
                
        return count