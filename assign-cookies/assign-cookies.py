class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        
        g.sort()
        s.sort()
        
        left = 0
        right = 0
        count = 0
        
        
        while left < len(g) and right < len(s):
            if s[right] >= g[left]:
                count += 1
                left += 1
                right += 1
            else:
                right += 1
                
        return count
                