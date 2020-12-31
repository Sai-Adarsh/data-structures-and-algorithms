class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        right = 0
        import sys
        minimum = sys.maxsize
        val_sum = 0
        
        while right < len(nums):
            val_sum += nums[right]
            while val_sum >= s:
                val_sum -= nums[left]
                minimum = min(minimum, right - left + 1)
                left += 1
            right += 1
        return minimum if minimum != sys.maxsize else 0
