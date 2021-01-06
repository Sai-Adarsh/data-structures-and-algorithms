class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        right = 0
        import sys
        max_length = sys.maxsize
        curr_sum = 0
​
        while right < len(nums):
            curr_sum += nums[right]
            while curr_sum >= s:
                max_length = min(max_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
​
        return max_length if max_length != sys.maxsize else 0
