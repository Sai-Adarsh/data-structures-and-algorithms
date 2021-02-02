class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        import sys
        diff = sys.maxsize
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                high = bisect.bisect(nums, complement, j + 1)
                low = high - 1
                if high < len(nums) and abs(complement - nums[high]) < abs(diff):
                    diff = complement - nums[high]
                if low > j and abs(complement - nums[low]) < abs(diff):
                    diff = complement - nums[low]
            if diff == 0:
                return target
        return target - diff
                    