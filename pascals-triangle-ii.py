class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums = [[1],[1,1]]
        if rowIndex == 0:
            return [1]
        if rowIndex < 2:
            return nums[-1]
        for i in range(rowIndex - 1):
            L = []
            for j in range(len(nums[-1]) + 1):
                if j == 0:
                    L.append(nums[-1][0])
                elif j == len(nums):
                    L.append(nums[-1][-1])
                else:
                    L.append(nums[-1][j] + nums[-1][j - 1])
            nums.append(L)
        return nums[-1]
