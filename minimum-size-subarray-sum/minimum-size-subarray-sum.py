class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        import sys
        min_subarray = sys.maxsize 
        curr_sum = 0
        
        while right < len(nums):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_subarray = min(min_subarray, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        
        return min_subarray if min_subarray != sys.maxsize else 0