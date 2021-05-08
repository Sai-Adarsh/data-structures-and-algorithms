class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        left = 0
        right = 0
        
        while left < len(t) and right < len(s):
            if t[left] != s[right]:
                left += 1
            else:
                left += 1
                right += 1
                
        return right == len(s)