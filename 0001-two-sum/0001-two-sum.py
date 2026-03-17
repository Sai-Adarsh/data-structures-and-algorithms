class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicesDict = defaultdict(list)
        for i in range(len(nums)):
            indicesDict[nums[i]].append(i)
        
        nums.sort()
        for i in range(len(nums)):
            complement = target - nums[i]
            index = bisect.bisect_left(nums, complement, i + 1)
            if i + 1 <= index <= len(nums) - 1 and nums[index] == complement:
                return [indicesDict[nums[i]].pop(0), indicesDict[nums[index]].pop(0)]