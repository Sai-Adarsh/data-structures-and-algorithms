class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])

        left = 0
        right = 1

        while right < len(intervals):
            if intervals[right][0] <= intervals[left][1]:
                intervals[left] = [min(intervals[left][0], intervals[right][0]), max(intervals[left][1], intervals[right][1])]
                del intervals[right]
            else:
                left = right
                right += 1

        return intervals