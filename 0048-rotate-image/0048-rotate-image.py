class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)

        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[N - j - 1][i]
                matrix[N - j - 1][i] = matrix[N - i - 1][N - j - 1]
                matrix[N - i - 1][N - j - 1] = matrix[j][N - i - 1]
                matrix[j][N - i - 1] = temp