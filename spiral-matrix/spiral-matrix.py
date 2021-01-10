class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        start_i = 0
        start_j = 0
        end_i = len(matrix)
        end_j = len(matrix[0])
​
        while len(res) < (len(matrix) * len(matrix[0])):
            #right
            for j in range(start_j, end_j):
                res.append(matrix[start_i][j])
            start_i += 1
            if len(res) == (len(matrix) * len(matrix[0])):
                break
​
​
            #bottom
            for i in range(start_i, end_i):
                res.append(matrix[i][end_j - 1])
            end_j -= 1
            if len(res) == (len(matrix) * len(matrix[0])):
                break
​
​
            #left
            for j in range(end_j - 1, start_j - 1, -1):
                res.append(matrix[end_i - 1][j])
            end_i -= 1
            if len(res) == (len(matrix) * len(matrix[0])):
                break
​
            #top
            for i in range(end_i - 1, start_i - 1, -1):
                res.append(matrix[i][start_j])
            start_j += 1
            if len(res) == (len(matrix) * len(matrix[0])):
                break
        return(res)
