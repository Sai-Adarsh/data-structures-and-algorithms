class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1], [1, 1]]

        for times in range(numRows - 2):
            temp = []
            temp.append(res[-1][0])
            for i in range(len(res[-1]) - 1):
                temp.append(res[-1][i] + res[-1][i + 1])

            temp.append(res[-1][-1])
            res.append(temp)
        return res[:numRows]