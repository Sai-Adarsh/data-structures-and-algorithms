class Solution:
    def intToRoman(self, num: int) -> str:
        num_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym_list = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        
        i = 12
        res = ""
        
        while num:
            quotient = num // num_list[i] # q = 3549 // 1000 = 3
            num = num % num_list[i]
            
            res += quotient * sym_list[i]
            i -= 1
        
        
        return res