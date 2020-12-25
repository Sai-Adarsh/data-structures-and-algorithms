class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(len(points)):
            if i + 1 < len(points):
                index_zero = max(points[i + 1][0], points[i][0]) - min(points[i + 1][0], points[i][0])
                index_one = max(points[i + 1][1], points[i][1]) - min(points[i + 1][1], points[i][1])
                count += max(index_zero, index_one)
        return count
