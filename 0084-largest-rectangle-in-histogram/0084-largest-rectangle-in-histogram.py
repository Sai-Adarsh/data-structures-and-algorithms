class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        res = 0
        heights.append(0)
        stack = [-1]
        
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                currHeight = heights[stack.pop()]
                currWidth = i - stack[-1] - 1
                res = max(res, currHeight * currWidth)
            
            stack.append(i)
            
        return res