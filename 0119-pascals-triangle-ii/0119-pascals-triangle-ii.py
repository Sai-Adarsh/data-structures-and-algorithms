class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        final = []

        for each in range(rowIndex + 1):
            if each == 0:
                temp = [1]
            elif each == 1:
                temp = [1, 1]
            else:
                prev = final[-1]
                temp = [prev[0]]
                for i in range(len(prev) - 1):
                    temp.append(prev[i] + prev[i + 1])
                temp.append(prev[-1])
            final.append(temp)
        
        return final[-1]