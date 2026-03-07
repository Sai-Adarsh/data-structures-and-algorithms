class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        resSet = set()
        resArr = list()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                low = j + 1
                high = len(nums) - 1
                while low < high:
                    totalSum = nums[i] + nums[j] + nums[low] + nums[high]
                    if totalSum == target:
                        temp = (nums[i], nums[j], nums[low], nums[high])
                        if temp not in resSet:
                            resSet.add(temp)
                            resArr.append([nums[i], nums[j], nums[low], nums[high]])
                        low += 1
                        high -= 1
                    elif totalSum > target:
                        high -= 1
                    else:
                        low += 1
        return resArr