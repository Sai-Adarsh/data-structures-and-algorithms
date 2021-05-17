class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        right = 0
        res = 0
        curr_prod = 1
        in_set = set()
        
        while right < len(nums):
            curr_prod *= nums[right]
            
            while curr_prod >= k:
                curr_prod //= nums[left]
                left += 1
            
            if tuple((left, right)) not in in_set:
                in_set.add(tuple((left, right)))
                res += (right - left + 1)
                
            right += 1
        return res
                
            