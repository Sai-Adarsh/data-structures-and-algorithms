class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        hashMap = defaultdict(list)

        currMax = -sys.maxsize - 1

        for i in range(len(nums)):
            if nums[i] > currMax:
                currMax = nums[i]
            hashMap[nums[i]].append(i)

        return hashMap[currMax][-1]