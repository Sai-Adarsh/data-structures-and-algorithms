class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        hash_set = {0: 1}
        
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if curr_sum % k == 0 and i >= 1:
                return True
            
            if curr_sum % k in hash_set:
                if i - hash_set[curr_sum % k] > 1:
                    return True
            else:
                hash_set[curr_sum % k] = i
                
        return False
                