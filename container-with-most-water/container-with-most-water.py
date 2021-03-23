class Solution:
    def maxArea(self, height: List[int]) -> int:
        import sys
        max_area = -sys.maxsize - 1
        left = 0
        right = len(height) - 1
        
        
        while left <= right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area