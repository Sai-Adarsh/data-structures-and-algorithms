class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        
        s = [i for i in s]
        
        left = 0
        right = 0
        curr_count = 0
        res = 0
        vowels = ["a", "e", "i", "o", "u"]
        
        while right < len(s):
            if s[right] in vowels:
                curr_count += 1
                
            if right - left + 1 == k:
                res = max(res, curr_count)
                if s[left] in vowels:
                    curr_count -= 1
                left += 1

            right += 1
            
        return res