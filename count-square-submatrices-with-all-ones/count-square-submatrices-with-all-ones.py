class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        
        
        curr_sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and j > 0 and matrix[i][j]:
                    matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1])
            curr_sum += sum(matrix[i])
        return curr_sum