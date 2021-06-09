class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        res = 0

        while True:
            if not nums:
                break
            else:
                res = max(res, sum([nums.pop(0), nums.pop()]))

        return(res)