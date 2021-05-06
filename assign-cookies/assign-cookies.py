class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        
        g.sort()
        s.sort()
        
        
        left = 0
        right = 0
        res = 0
        
        # greed is to satisfy
        # if current s[j] >= g[i] (can satisfy) left = right, right += 1, count
        # else move until the cookie can satify current greed. right += 1
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                res += 1
                left += 1
                right += 1
            else:
                right += 1
                
        return res