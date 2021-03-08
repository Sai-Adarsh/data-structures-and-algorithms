class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    
        intervals.sort(key = lambda x: x[0])
        
        left = 0
        right = 1
        count = 0
        
        while right < len(intervals):
            if intervals[left][1] <= intervals[right][0]:
                left = right
                right += 1
            elif intervals[left][1] <= intervals[right][1]:
                count += 1
                right += 1
            elif intervals[left][0] <= intervals[right][0]:
                count += 1
                left = right
                right += 1
        return count