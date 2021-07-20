class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        
        def countGenerator(pattern):
            res = []
            hash_map = {}
            count = 0
            for i in pattern:
                if i not in hash_map:
                    hash_map[i] = count
                    count += 1
                res.append(hash_map[i])
            return res
        
        pattern = countGenerator(pattern)
        
        L = []
        for i in words:
            if pattern == countGenerator(i):
                L.append(i)
        return L