class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        resSet = set()
        resList = list()
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                total = nums[i] + nums[low] + nums[high]
                if total == 0:
                    temp = (nums[i], nums[low], nums[high])
                    if temp not in resSet:
                        resSet.add(temp)
                        resList.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                elif total > 0:
                    high -= 1
                else:
                    low += 1
        return resList