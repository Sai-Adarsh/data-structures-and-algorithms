class Solution:
    def rob(self, nums: List[int]) -> int:

        # 1, 2, 4, 4
        # max(nums[i] + dp[-2], dp[-1])

        if len(nums) == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            dp.append(max(nums[i] + dp[-2], dp[-1]))

        return dp[-1]