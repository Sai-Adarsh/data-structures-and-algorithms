class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = 0
        res = 0
        currProd = 1
        
        
        while right < len(nums):
            currProd *= nums[right]
            
            while currProd >= k and left <= right:
                currProd //= nums[left]
                left += 1
            
            
            res += right - left + 1
            right += 1
            
        return res