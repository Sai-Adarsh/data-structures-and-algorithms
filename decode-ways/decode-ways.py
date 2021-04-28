class Solution:
    def numDecodings(self, s: str) -> int:
        
        decodable = {str(i) for i in range(1, 27)}
        
        @cache
        def numways(i):
            if i == len(s):
                return 1
            
            res = 0
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in decodable:
                    res += numways(j)
                        
            return res
        
        return numways(0)