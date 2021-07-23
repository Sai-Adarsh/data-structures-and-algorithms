class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        s = collections.Counter(nums)
        res = 0
        
        for i in s:
            if i + 1 in s:
                res = max(s[i] + s[i + 1], res)
                
                
        return res