class Solution:
    def baseNeg2(self, n: int) -> str:
        N = n
        string = ''
        while N != 0:
            if N % 2:
                string += '1'
                N -= 1
            else:
                string += '0'
            N //= -2
        return string[::-1] if string else '0'