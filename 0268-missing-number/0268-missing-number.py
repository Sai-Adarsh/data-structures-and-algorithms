class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

        N = len(nums)
        return list(set([i for i in range(N + 1)]) - set(nums))[0]