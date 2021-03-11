class Solution:
    def intToRoman(self, num: int) -> str:
        def printRoman(number):
            num = [1, 4, 5, 9, 10, 40, 50, 90, 
                   100, 400, 500, 900, 1000]
            sym = ["I", "IV", "V", "IX", "X", "XL", 
                   "L", "XC", "C", "CD", "D", "CM", "M"]
            i = 12
            res = ""
            while number:
                div = number // num[i]
                number %= num[i]

                while div:
                    res += sym[i]
                    div -= 1
                i -= 1
            return res
 
        number = num
        return printRoman(number)