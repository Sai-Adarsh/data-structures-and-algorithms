class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        
        
        
        nums = ["a", "e", "i", "o", "u"]
        
        @cache
        def backTracking(start, pos):
            if pos == n:
                return 1
            
            res = 0
            
            for i in range(len(nums)):
                if nums[i] >= nums[start]:
                    res += backTracking(i, pos + 1)
                
            return res
        
        return backTracking(0, 0)