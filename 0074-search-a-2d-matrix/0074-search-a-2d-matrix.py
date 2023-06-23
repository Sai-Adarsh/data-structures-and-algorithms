class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            isThere = bisect.bisect_left(matrix[i], target)
            if 0 <= isThere <= len(matrix[i]) - 1:
                if matrix[i][isThere] == target:
                    return True
        return False