class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        n = len(matrix[0])
        left, right, height = [0]*n, [n]*n, [0]*n
        res = 0
        
        for row in matrix:
            # calculate right
            currentRight = n      
            for i in range(n-1,-1,-1):
                if row[i] == '1':
                    right[i] = min(right[i],currentRight)
                else:
                    right[i] = n 
                    currentRight = i
            
            currentLeft = 0
            for i in range(n):
                # calculate height
                height[i] = height[i]+1 if row[i] == '1' else 0
                # calculate left
                if row[i] == '1':
                    left[i] = max(left[i],currentLeft)
                else:
                    left[i] = 0
                    currentLeft = i+1
                # calculate Rectangle
                res = max(res,height[i]*(right[i]-left[i]))
                    
        return res