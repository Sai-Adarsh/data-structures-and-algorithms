class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        right = 0
        sub_sum = 0
        curr_prod = 1
        
        while right <= len(nums) - 1:
            curr_prod = curr_prod * nums[right]
            while curr_prod >= k:
                curr_prod /= nums[left]
                left += 1
            sub_sum += (right - left + 1)
            right += 1
                
        return sub_sum