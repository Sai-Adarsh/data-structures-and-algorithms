class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        hash_set = collections.Counter()
        
        left = 0
        right = 0
        max_count = 0
        res = 0
        
        while right < len(s):
            hash_set[s[right]] += 1
            max_count = max(max_count, hash_set[s[right]])
            
            while right - left - max_count + 1 > k:
                hash_set[s[left]] -= 1
                left += 1
                
                
            res = max(res, right - left + 1)
            right += 1
        return res
                