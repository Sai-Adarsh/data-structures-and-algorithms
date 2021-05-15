class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        master = [[1], [1, 1]]
        
        if rowIndex == 0:
            return master[0]
        if rowIndex == 1:
            return master[1]
        
        for i in range(2, rowIndex + 1):
            temp = [1]
            for j in range(len(master[-1]) - 1):
                temp.append(master[-1][j] + master[-1][j + 1])
            temp.append(1)
            master.append(temp)

        return master[rowIndex]