class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Kadane's algorithm
        
        meh = 0
        msf = -sys.maxsize
        
        for i in range(len(nums)):
            meh += nums[i]
            
            if meh < nums[i]:
                meh = nums[i]
            
            if msf < meh:
                msf = meh
                
        return msf