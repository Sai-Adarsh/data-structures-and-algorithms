class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # 1 2 2 3 8
        # 0 1 1 3 4
        
        backup = []
        backup[:] = nums[:]
        
        nums.sort()
        hash_map = defaultdict(list)
        
        
        for i in range(len(nums)):
            hash_map[nums[i]].append(i)
            
        res = []
        for i in backup:
            res.append(min(hash_map[i]))
            
        return res