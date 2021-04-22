class Solution:
    def numSquares(self, n: int) -> int:
        arr = []
        i = 1
        while True:
            if i * i > n:
                break
            else:
                arr.append(i*i)
                i += 1
        import sys
        @cache
        def backTracking(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            res = sys.maxsize
            for i in range(len(arr)):
                if amount - arr[i] >= 0:
                    res = min(res, backTracking(amount - arr[i]) + 1)
            return res
        L = backTracking(n)
        return L if L != sys.maxsize else n