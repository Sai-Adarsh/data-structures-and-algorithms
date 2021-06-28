class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        left = 0
        right = 0
        hash_map = collections.Counter()
        res = 0
        
        while right < len(s):
            hash_map[s[right]] += 1
            
            while hash_map["a"] > 0 and hash_map["b"] > 0 and hash_map["c"] > 0:
                res += len(s) - right
                hash_map[s[left]] -= 1
                left += 1
                
            
            right += 1
            
        return res