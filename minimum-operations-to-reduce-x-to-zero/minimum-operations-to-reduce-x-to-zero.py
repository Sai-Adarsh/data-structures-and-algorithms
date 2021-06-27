class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

    
        hash_map = {}
        curr_sum = 0
        ans = sys.maxsize
        hash_map[0] = len(nums)
        for i in range(len(nums) -1, -1, -1):
            curr_sum += nums[i]
            hash_map[curr_sum] = i
            if curr_sum == x:
                ans = min(ans, len(nums) - i)
                
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if x - curr_sum in hash_map:
                if hash_map[x - curr_sum] > i:
                    ans = min(ans, len(nums) - hash_map[x - curr_sum] + i + 1)
        
        if ans == sys.maxsize:
            return -1
        return ans