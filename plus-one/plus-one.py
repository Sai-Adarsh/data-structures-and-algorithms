class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        L = int("".join([str(i) for i in digits])) + 1
        L = [int(i) for i in str(L)]
        from collections import deque
        if len(digits) != len(L):
            zfillValue = len(digits) - len(L)
            L = deque(L)
            for i in range(zfillValue):
                L.appendleft(0)
            return list(L)
        else:
            return L
