class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s = [i.upper() for i in s if i.isalnum()]
        i = k
        s = s[::-1]
        while i < len(s):
            s.insert(i, "-")
            i += (k + 1)
        return "".join(s[::-1])