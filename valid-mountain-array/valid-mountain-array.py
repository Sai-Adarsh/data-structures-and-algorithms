class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        A = arr
        if sorted(A) == A:
            return False
        elif sorted(A, reverse = True) == A:
            return False
        else:
            i = 0
            N = len(A)
            while i + 1 < N:
                if A[i] < A[i + 1]:
                    i += 1
                else:
                    break
            if i == N - 1 or i == 0:
                return False
            while i + 1 < N:
                if A[i] > A[i + 1]:
                    i += 1
                else:
                    break
            return i == N - 1
