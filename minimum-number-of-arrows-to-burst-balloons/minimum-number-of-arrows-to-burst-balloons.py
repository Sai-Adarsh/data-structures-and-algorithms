class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x: x[1])
        print(points)
        
        arrow = 1
        end = points[0][1]
        
        i = 1
        while i < len(points):
            if points[i][0] > end:
                arrow += 1
                end = points[i][1]
            i += 1
        return arrow