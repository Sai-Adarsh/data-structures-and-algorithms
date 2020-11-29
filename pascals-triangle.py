class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = [[1],[1,1]]
        if numRows == 0:
            return []
        if numRows < 3:
            return nums[:numRows]
        for i in range(numRows - 2):
            L = []
            for j in range(len(nums[-1]) + 1):
                if j == 0:
                    L.append(nums[-1][0])
                elif j == len(nums):
                    L.append(nums[-1][-1])
                else:
                    L.append(nums[-1][j] + nums[-1][j - 1])
            nums.append(L)
        return nums
