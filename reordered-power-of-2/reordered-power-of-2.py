class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        from itertools import permutations
        L = list(map(list, permutations(str(N))))
        L = ["".join(i) for i in L if i[0] != "0" and bin(int("".join(i))).count("1") == 1]
        return len(L) >= 1