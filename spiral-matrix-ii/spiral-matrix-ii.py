class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        numerals = n * n
        matrix = []
        left = 1
        right = n + 1
        for i in range(n):
​
            matrix.append([x for x in range(left, right)])
            left += n
            right += n
        #print(matrix)
        res = []
        dp = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        start_i = 0
        start_j = 0
        end_i = len(matrix)
        end_j = len(matrix[0])
​
        start = 1
        while len(res) < len(matrix) * len(matrix[0]):
            for j in range(start_j, end_j):
                res.append(matrix[start_i][j])
                dp[start_i][j] = start
                start += 1
            start_i += 1
