class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    
    
        return self.backTracking(candidates, [], 0, [], target)
    
    def backTracking(self, nums, res, divider, path, target):
        #base case
        if target <= 0:
            if target == 0:
                if sorted(path) not in res:
                    res.append(sorted(path))
            return
        #recursive case
        i = divider
        for i in range(divider, len(nums)):
            if i > divider and nums[i] == nums[i - 1]:
                continue
            self.backTracking(nums, res, i + 1, path + [nums[i]], target - nums[i])
            i += 1
        return res