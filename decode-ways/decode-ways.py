class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        ascii_list = [_ for _ in range(1, 27)]
        
        @cache
        def backTracking(start):
            if start == len(s):
                return 1
            
            res = 0
            for i in range(start + 1, len(s) + 1):
                sub_string = s[start : i]
                if int(sub_string) in ascii_list and len(sub_string) == len(str(int(sub_string))):
                    res += backTracking(i)
                    
            return res
        
        L = backTracking(0)
        return L
                    
            