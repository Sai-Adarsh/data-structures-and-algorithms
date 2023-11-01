class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowHasZero, colHasZero = False, False 

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                colHasZero = True
                break

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                rowHasZero = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        
        def zeroRows(i):
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        def zeroCols(j):
            for i in range(len(matrix)):
                matrix[i][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                zeroRows(i)

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                zeroCols(j)

        if rowHasZero:
            zeroRows(0)
        
        if colHasZero:
            zeroCols(0)