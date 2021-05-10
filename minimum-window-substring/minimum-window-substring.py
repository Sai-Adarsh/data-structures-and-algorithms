class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        lookup = collections.Counter(t)
        
        output = ""
        maxi = sys.maxsize
        
        left = 0
        right = 0
        
        count = len(lookup)
        
        while right < len(s):
            while right < len(s) and count != 0:
                if s[right] in lookup:
                    lookup[s[right]] -= 1
                    if lookup[s[right]] == 0:
                        count -= 1
                right += 1
                
            while left < right and count == 0:
                if right - left < maxi:
                    maxi = right - left
                    output = s[left: right]
                if s[left] in lookup:
                    lookup[s[left]] += 1
                    if lookup[s[left]] >= 1:
                        count += 1
                left += 1
                
        return output