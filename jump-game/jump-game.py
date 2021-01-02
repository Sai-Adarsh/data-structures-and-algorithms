class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGoodIndex = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if lastGoodIndex <= nums[i] + i:
                lastGoodIndex = i
        return lastGoodIndex == 0
