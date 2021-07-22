class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        
        
        max_arr = [nums[0]]
        min_arr = [nums[-1]]
        
        for i in range(1, len(nums)):
            max_arr.append(max(max_arr[-1], nums[i]))
        
        for i in range(len(nums) -2, -1, -1):
            min_arr.append(min(min_arr[-1], nums[i]))
            
        min_arr = min_arr[::-1]
        
        for i in range(len(nums) - 1):
            if max_arr[i] <= min_arr[i + 1]:
                return i + 1