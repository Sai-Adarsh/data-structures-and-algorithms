class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        left = 0
        right = left + 1

        while right < len(intervals):
            if intervals[left][1] >= intervals[right][0]:
                temp = [min(intervals[left][0], intervals[right][0]), max(intervals[left][1], intervals[right][1])]
                intervals[left] = temp
                del intervals[right]
            else:
                left += 1
                right += 1

        return intervals