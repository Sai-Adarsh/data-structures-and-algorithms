class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        maxEndingHereN=nums[0]
        
        maxEndingHereP=nums[0]
        
        maxSoFar=abs(nums[0])
        
        for i in nums[1:]:
            maxEndingHereN+=i
            maxEndingHereP+=i
            if(i<maxEndingHereN):
                maxEndingHereN=i
            if(i>maxEndingHereP):
                maxEndingHereP=i
            maxSoFar=max(abs(maxEndingHereN),abs(maxEndingHereP),maxSoFar)
        return maxSoFar