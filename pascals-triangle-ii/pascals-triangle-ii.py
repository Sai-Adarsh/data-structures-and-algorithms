class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        dp = [[1], [1, 1]]

        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]

        for i in range(rowIndex - 2 + 1):
            temp = []
            temp.append(1)
            for j in range(len(dp[-1]) - 1):
                temp.append(dp[-1][j] + dp[-1][j + 1])
            temp.append(1)
            dp.append(temp)

        return dp[-1]