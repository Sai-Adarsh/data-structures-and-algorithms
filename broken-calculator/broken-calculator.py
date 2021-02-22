class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X > Y:
            return X - Y
        res = 0
        while Y > X:
            res += 1
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
        return res + (X - Y)