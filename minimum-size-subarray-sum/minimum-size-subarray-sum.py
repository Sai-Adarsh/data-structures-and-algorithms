class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        right = 0
        
        curr_sum = 0
        res = sys.maxsize
        
        while right < len(nums):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1
                
            right += 1
            
        return res if res != sys.maxsize else 0