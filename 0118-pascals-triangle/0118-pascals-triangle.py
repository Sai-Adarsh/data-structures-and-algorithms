class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = [[1], [1, 1]]

        for each in range(2, numRows):
            temp = [final[-1][0]]
            for i in range(len(final[-1]) - 1):
                temp.append(final[-1][i] + final[-1][i + 1])
            temp.append(final[-1][-1])
            final.append(temp)
        return final[:numRows]