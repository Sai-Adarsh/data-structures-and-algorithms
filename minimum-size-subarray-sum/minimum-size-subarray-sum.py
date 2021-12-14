class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        left = 0
        right = 0
        currSum = 0
        res = sys.maxsize
        
        while right < len(nums):
            currSum += nums[right]
            
            while currSum >= target:
                res = min(res, right - left + 1)
                currSum -= nums[left]
                left += 1
            
            right += 1
            
        return res if res != sys.maxsize else 0