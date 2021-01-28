class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = 'a' * n
        res = [i for i in res]
        k = k - n
        for i in range(len(res) -1, -1, -1):
            if k >= 26:
                res[i] = 'z'
                k = k - 26 + 1
            else:
                res[i] = chr(k + 97)
                break
        return "".join(res)