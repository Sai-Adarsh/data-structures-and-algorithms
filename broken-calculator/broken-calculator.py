class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X > Y:
            return X - Y
        res = 0
        while Y > X:
            if Y % 2 == 0:
                res += 1
                Y //= 2
            else:
                res += 1
                Y += 1
        return res + (X - Y)
                    
                    