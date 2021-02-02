class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        added = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    complement = target - nums[i] - nums[j] - nums[k]
                    is_there = bisect.bisect_left(nums, complement, k + 1)
                    
                    if is_there < len(nums):
                        if nums[is_there] == complement:
                            temp = sorted([complement, nums[i], nums[j], nums[k]])
                            if temp not in res:
                                res.append(temp)
        return res