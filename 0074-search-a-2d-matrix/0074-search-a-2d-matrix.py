class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                isThere = bisect.bisect_left(matrix[i], target)
                if 0 <= isThere <= len(matrix[i]) and matrix[i][isThere] == target:
                    return True

        return False