class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        return len([s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j] == s[i:j][::-1]])