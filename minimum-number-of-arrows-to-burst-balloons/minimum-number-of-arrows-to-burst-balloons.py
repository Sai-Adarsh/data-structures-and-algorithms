class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key = lambda x: x[1])
        
        arrow = 1
        left = 0
        right = 1
        
        while right < len(points):
            if points[left][1] < points[right][0]:
                arrow += 1
                left = right
            right += 1
        return arrow