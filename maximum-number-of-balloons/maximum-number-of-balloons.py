class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        s = "balloon"
        hash_map = collections.Counter(text)
        
        if not (hash_map["a"] >= 1 and hash_map["b"] >= 1 and hash_map["n"] >= 1 and hash_map["l"] >= 2 and hash_map["o"] >= 2):
            return 0
        
        res = 0
        start = 0
        while True:
            if hash_map[s[start]] == 0:
                break
            else:
                hash_map[s[start]] -= 1
                start += 1
                if start == len(s):
                    start = 0
                    res += 1
                    
        return res