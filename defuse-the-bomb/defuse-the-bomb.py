class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        nums = code
        L = nums * 3
        res = []
        for i in range(len(nums), 2 * len(nums)):
            if k > 0:
                res.append(sum(L[i + 1: i + k + 1]))
            elif k < 0:
                res.append(sum(L[i + k: i]))
            else:
                res.append(0)

        return(res)