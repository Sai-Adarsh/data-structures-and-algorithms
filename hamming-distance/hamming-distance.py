class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x).zfill(64).replace("0b", "")
        y = bin(y).zfill(64).replace("0b", "")
​
        res = 0
        for i in range(len(x) - 1, -1, -1):
            if x[i] != y[i]:
                res += 1
        return(res)
