class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        
        num = int(num)
        
        while num > 0:
            if num % 2 != 0:
                return str(num)
            else:
                num //= 10
        
        return ""