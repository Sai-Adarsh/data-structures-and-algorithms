class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if matrix[i][-1] < target:
                continue
            else:
                index = bisect.bisect_left(matrix[i], target)
                if 0 <= index <= len(matrix[i]) - 1 and matrix[i][index] == target:
                    return True

        return False