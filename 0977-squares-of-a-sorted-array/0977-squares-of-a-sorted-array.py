class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            bisect.insort(res, i * i)
        return res