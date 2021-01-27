class Solution:
    def concatenatedBinary(self, n: int) -> int:
        L = [bin(i).replace("0b", "") for i in range(1, n + 1)]
        res = ""
        for i in L:
            res += i
        return int(res, 2) % ((10 ** 9) + 7)