class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        left = 0
        right = 1

        while right < len(intervals):
            x1, y1 = intervals[left]
            x2, y2 = intervals[right]
            if y1 >= x2:
                x = min(x1, x2)
                y = max(y1, y2)
                intervals[left] = [x, y]
                del intervals[right]
            else:
                left += 1
                right += 1                

        return intervals