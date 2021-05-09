class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        
        @cache
        def backTracking(i, prev_state):
            if i == 0:
                return 1
            
            return 1 + backTracking(i - 1, -prev_state) if (nums[i] - nums[i - 1]) * prev_state < 0 else backTracking(i - 1, prev_state)
            
            
        return max(backTracking(len(nums) - 1, -1), backTracking(len(nums) - 1, 1))