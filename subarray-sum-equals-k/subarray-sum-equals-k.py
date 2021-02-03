class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        res = 0
        hash_map = {0: 1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in hash_map:
                res += hash_map[sum - k]
            if sum not in hash_map:
                hash_map[sum] = 1
            else:
                hash_map[sum] += 1
                
        return res