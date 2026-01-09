class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n == len(original):
            res = []
            curr = []
            for each in original:
                curr.append(each)
                if len(curr) == n:
                    res.append(curr)
                    curr = []
            return res
        else:
            return []