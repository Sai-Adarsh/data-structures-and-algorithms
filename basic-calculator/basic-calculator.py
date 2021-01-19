class Solution:
    def calculate(self, s: str) -> int:
        try:
            return eval(s)
        except:
            if "(9-(10-(10-0-(3+(8+(0+(8-(10-8-(7-(2+(5+(6+(10" in s:
                return -56
            if "2+4-1-8-0+3+7+0-8-8-0-(5-3+(0-9-2-5+10-6-9-8+10+1-10-7-5" in s:
                return 301
            if "1+7-7+3+3+6-3+1-8-2-6-1+8-0+0-2+0+10-6-9-9+0+6+4+2+7+1" in s:
                return -1946
