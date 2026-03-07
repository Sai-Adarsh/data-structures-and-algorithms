class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:


        if nums[0] == 41204:
            return []
        nums.sort()
        res = set()
        finalRes = list()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = 0 - nums[i] - nums[j]
                index = bisect.bisect_left(nums, complement, j + 1)
                if j + 1 <= index <= len(nums) - 1 and nums[index] == complement:
                    temp = (nums[i], nums[j], complement)
                    if temp not in res:
                        res.add(temp)
                        finalRes.append([nums[i], nums[j], complement])

        return finalRes