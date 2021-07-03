class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        ascii_list = [_ for _ in range(1, 27)]
        
        @cache
        def backTracking(s):
            if not s:
                return 1
                
            res = 0
            for i in range(1, len(s) + 1):
                sub_string = s[0 : i]
                if len(sub_string) == len(str(int(sub_string))):
                    if int(sub_string) in ascii_list:
                        res += backTracking(s[i : ])
                    
            return res
        L = backTracking(s)
        return L