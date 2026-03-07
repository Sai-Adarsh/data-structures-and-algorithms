class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        resSet = set()
        resArr = list()

        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1

            while low < high:
                totalSum = nums[i] + nums[low] + nums[high]
                if totalSum == 0:
                    temp = (nums[i], nums[low], nums[high])
                    if temp not in resSet:
                        resSet.add(temp)
                        resArr.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                elif totalSum > 0:
                    high -= 1
                else:
                    low += 1
        return resArr