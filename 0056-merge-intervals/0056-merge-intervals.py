class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        left = 0
        right = 1

        while right < len(intervals) and left < right:
            if intervals[left][1] >= intervals[right][0]:
                newLeft = min(intervals[left][0], intervals[right][0])
                newRight = max(intervals[left][1], intervals[right][1])
                temp = [newLeft, newRight]
                intervals[left] = temp
                del intervals[right]
            else:
                left += 1
                right += 1
        return intervals