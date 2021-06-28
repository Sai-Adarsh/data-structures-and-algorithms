class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        
        left = 0
        right = 0
        hash_set = collections.Counter()
        res = 0
        while right < len(s):
            hash_set[s[right]] += 1
            
            while hash_set["a"] > 0 and hash_set["b"] > 0 and hash_set["c"] > 0:
                res += len(s) - right
                hash_set[s[left]] -= 1
                left += 1
                
            right += 1
            
        return (res)