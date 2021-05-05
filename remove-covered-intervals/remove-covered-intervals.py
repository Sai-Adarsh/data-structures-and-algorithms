class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], -x[1]))
        
        i = 0
        ending = 0
        res = 0
        
        while i < len(intervals):
            if intervals[i][1] > ending:
                ending = intervals[i][1]
                res += 1
            
            i += 1
            
        return res