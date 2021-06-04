class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        left = 0
        right = 0
        hash_map = collections.Counter()
        max_res = 0
        res = 0
        
        while right < len(s):
            hash_map[s[right]] += 1
            max_res = max(max_res, hash_map[s[right]])
            
            while right - left - max_res + 1 > k:
                hash_map[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
            
        return res
                