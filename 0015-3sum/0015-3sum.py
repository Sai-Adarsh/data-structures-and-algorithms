class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        res = list()
        nums.sort()

        # -4, -1, -1, 0, 1, 2

        for i in range(len(nums)):
            complement = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > complement:
                    right -= 1
                elif nums[left] + nums[right] < complement:
                    left += 1
                else:
                    temp = (nums[i], nums[left], nums[right])
                    if temp not in ans:
                        ans.add(temp)
                        res.append(temp)
                    left += 1
                    right -= 1
        return res