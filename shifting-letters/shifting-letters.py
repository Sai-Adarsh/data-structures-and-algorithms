class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = [i for i in s]

        from itertools import accumulate
        shifts = list(accumulate(shifts[::-1]))[::-1]
        
        res = ""
        
        for i in range(len(s)):
            L = (ord(s[i])) + shifts[i] % 26

            
            if 97 <= L <= 122:
                res += chr(L)
            else:
                res += chr(96 + L % 122) 

        return res