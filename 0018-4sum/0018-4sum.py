class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - (nums[i] + nums[j])
                # target = 10
                # 2, 4 = 2 + 4 = 6
                # 10 - (2 + 4)
                # 10 - (6)
                # 4
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    currSum = nums[left] + nums[right]
                    if currSum > complement:
                        right -= 1
                    elif currSum < complement:
                        left += 1
                    else:
                        temp = sorted([nums[i], nums[j], nums[left], nums[right]])
                        if temp not in res:
                            res.append(temp)
                        right -= 1
                        left += 1
        return res