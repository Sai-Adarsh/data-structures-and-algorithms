class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        res = ""
        
        while True:
            if a == 0 and b == 0:
                break
                
            if a > b and a > 0 and b > 0:
                res += "aab"
                a -= 2
                b -= 1
            if b > a and a > 0 and b > 0:
                res += "bba"
                a -= 1
                b -= 2
            if a == b and a > 0 and b > 0:
                res += "ab"
                a -= 1
                b -= 1
            if a > b and b == 0:
                res += "a" * a
                a = 0
            if b > a and a == 0:
                res += "b" * b
                b = 0
                
        return res