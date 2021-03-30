class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        import sys
        meh = 0
        msf = -sys.maxsize - 1
        
        for i in range(len(nums)):
            meh = meh + nums[i]
            if meh < nums[i]:
                meh = nums[i]
            if msf < meh:
                msf = meh
        return msf