class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        hash_set = {0: 1}
        curr_sum = 0
        res = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            
            if curr_sum % k in hash_set:
                res += hash_set[curr_sum % k]
                hash_set[curr_sum % k] += 1
            else:
                hash_set[curr_sum % k] = 1
                
        return res