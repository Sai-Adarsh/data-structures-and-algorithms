class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums)
        
    def helper(self, nums):
        nums.sort()
        added = set()
        res = []
        
        for i in range(len(nums) - 1, -1, -1):
            last = nums[i]
            start, end = 0, i - 1
            while start < end:
                temp = last + nums[start] + nums[end]
                if temp == 0:
                    if (last, nums[start], nums[end]) not in added:
                        res.append([last, nums[start], nums[end]])
                    added.add((last, nums[start], nums[end]))
                    start += 1
                elif temp > 0:
                    end -= 1
                else:
                    start += 1
        return res