class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, cols = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for eachRow in rows:
            for j in range(len(matrix[0])):
                matrix[eachRow][j] = 0

        for eachCol in cols:
            for i in range(len(matrix)):
                matrix[i][eachCol] = 0

        return matrix