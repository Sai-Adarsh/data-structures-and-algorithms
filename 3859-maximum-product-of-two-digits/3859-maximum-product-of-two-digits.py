class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []
        while True:
            if not n:
                break
            else:
                bisect.insort(arr, n % 10)
                n = n // 10

        if len(arr) >= 2:
            return arr[-1] * arr[-2]
        