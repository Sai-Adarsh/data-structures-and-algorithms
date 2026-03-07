class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        originalIndices = defaultdict(list)
        for i in range(len(nums)):
            originalIndices[nums[i]].append(i)

        nums.sort()
        for i in range(len(nums)):
            findTarget = target - nums[i]
            index = bisect.bisect_left(nums, findTarget, i)
            if i <= index <= len(nums) - 1 and nums[index] == findTarget:
                return [originalIndices[nums[i]].pop(), originalIndices[findTarget].pop()]