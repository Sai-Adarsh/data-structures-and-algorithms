class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        hash_set = {}
        i = 0
        res = []
        while i < len(nums):
            if nums[i] not in hash_set:
                hash_set[nums[i]] = i
                res.append(nums[i])
            i += 1
        nums[:] = res
        return len(nums)
                