class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash_set = {}
        i = 0
        
        while i < len(nums):
            if nums[i] not in hash_set:
                hash_set[nums[i]] = 1
                i += 1
            else:
                hash_set[nums[i]] = 2
                nums.remove(nums[i])
        return len(nums)
