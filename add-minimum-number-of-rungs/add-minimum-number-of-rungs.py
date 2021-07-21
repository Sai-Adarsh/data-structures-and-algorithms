class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        L, count = 0, 0
        for i in rungs:
            if (i - L) > dist:
                count += (i - L - 1) // dist
            L = i
        return count