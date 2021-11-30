class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        isThere = bisect.bisect_left(nums, target)
        return isThere