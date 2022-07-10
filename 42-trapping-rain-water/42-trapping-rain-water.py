class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        left = [0 for _ in range(len(height))]
        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])
            
            
        right = [0 for _ in range(len(height))]
        right[-1] = height[-1]
        for j in range(len(height) - 2, -1, -1):
            right[j] = max(right[j + 1], height[j])
            
        
        for i in range(len(height)):
            res += min(left[i], right[i]) - height[i]
            
        return res