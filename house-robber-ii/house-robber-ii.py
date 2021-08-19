class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[-1]
    
        if len(nums) == 2:
            return max(nums[-1], nums[-2])
        
        one = nums[:-1]
        two = nums[1:]
        
        dp_one = [one[0], max(one[0], one[1])]
        dp_two = [two[0], max(two[0], two[1])]
        
        for i in range(2, len(one)):
            dp_one.append(max(dp_one[-1], dp_one[-2] + one[i]))
            
        for i in range(2, len(two)):
            dp_two.append(max(dp_two[-1], dp_two[-2] + two[i]))
            
        return max(dp_one[-1], dp_two[-1])