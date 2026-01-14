class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = sys.maxsize
        res = 0

        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1

            while low < high:
                currSum = nums[i] + nums[low] + nums[high]
                currDiff = abs(currSum - target)

                if currDiff < diff:
                    res = currSum
                    diff = currDiff

                if currSum < target:
                    low +=1
                elif currSum > target:
                    high -= 1
                else:
                    return currSum

        return res