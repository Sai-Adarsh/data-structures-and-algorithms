class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        from itertools import permutations
        L = list(permutations(arr))
        try:
            L = list(filter(lambda x: int("".join([str(i) for i in list(x[:2])])) < 24 and int("".join([str(i) for i in list(x[2:])])) < 60, L))
            L.sort()
            L = L[-1]
            return("".join([str(i) for i in L[:2]]) + ":" + "".join([str(i) for i in L[2:]]))
        except:
            return ""
