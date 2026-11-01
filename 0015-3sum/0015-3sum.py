class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()
        finalAns = list()
        nums.sort()
        target = 0

        for i in range(len(nums)):
            complement = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                currSum = nums[left] + nums[right] + nums[i]
                if currSum > target:
                    right -= 1
                elif currSum < target:
                    left += 1
                else:
                    temp = sorted([nums[left], nums[right], nums[i]])
                    temp = tuple(temp)
                    if temp not in ans:
                        ans.add(temp)
                        finalAns.append(temp)
                    right -= 1
                    left += 1
        return finalAns