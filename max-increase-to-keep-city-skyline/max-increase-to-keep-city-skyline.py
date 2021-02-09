class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        from numpy import transpose
        presum = sum([sum(i) for i in grid])
        rowMax = [max(i) for i in grid]
        colMax = [max(i) for i in transpose(grid)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = min(rowMax[i], colMax[j])
        return sum([sum(i) for i in grid]) - presum