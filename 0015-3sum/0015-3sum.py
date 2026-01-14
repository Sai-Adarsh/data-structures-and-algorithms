class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        hashMap = {}
        res = []
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1

            while low < high:
                tempSum = nums[i] + nums[low] + nums[high]
                if tempSum == 0:
                    temp = (nums[i], nums[low], nums[high])
                    if temp not in hashMap:
                        hashMap[temp] = 1
                        res.append(temp)
                    else:
                        hashMap[temp] = 2
                    low += 1
                    high -= 1
                elif tempSum > 0:
                    high -= 1
                else:
                    low += 1
        return res