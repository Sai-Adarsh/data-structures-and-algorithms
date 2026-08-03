class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indicesMap = defaultdict(list)

        for i in range(len(nums)):
            indicesMap[nums[i]].append(i)

        nums.sort()

        left = 0
        right = len(nums) - 1

        while left < right:
            currSum = nums[left] + nums[right]
            if currSum > target:
                right -= 1
            elif currSum < target:
                left += 1
            else:
                return [indicesMap[nums[left]].pop(), indicesMap[nums[right]].pop()]
