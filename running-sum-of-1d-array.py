class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(nums[i] + res[i - 1])
        return(res)
