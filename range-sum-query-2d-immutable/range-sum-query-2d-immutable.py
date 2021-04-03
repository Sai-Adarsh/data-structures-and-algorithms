class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return
        
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[i][j + 1] = dp[i][j] + matrix[i][j]
        
        self.dp = dp
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2 + 1):
            sum += self.dp[row][col2 + 1] - self.dp[row][col1]
        return sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)