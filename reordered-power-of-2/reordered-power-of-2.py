class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # how is a number converted to binary
        # all powers of two's binary has ones at only one place
        from itertools import permutations
        L = list(map("".join, permutations(str(N))))
        L = ["".join(i) for i in L if "".join(i)[0] != "0" and bin(int("".join(i))).count("1") == 1]
        return len(L) >= 1