class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        lookup = collections.Counter(t)
        
        left = 0
        right = 0
        max_len = sys.maxsize
        output = ""
        
        count = len(lookup)
        
        while right < len(s):
            while right < len(s) and count != 0:
                if s[right] in lookup:
                    lookup[s[right]] -= 1
                    if lookup[s[right]] == 0:
                        count -= 1
                    
                right += 1
            
            while left < right and count == 0:
                if right - left < max_len:
                    max_len = right - left
                    output = s[left:right]
                if s[left] in lookup:
                    lookup[s[left]] += 1
                    if lookup[s[left]] >= 1:
                        count += 1
                        
                left += 1
        return output