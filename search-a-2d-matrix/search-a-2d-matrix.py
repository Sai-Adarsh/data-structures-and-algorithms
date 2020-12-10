class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            left = 0
            right = len(i) - 1
            while left <= right:
                curr = left + (right - left) // 2
                if target > i[curr]:
                    left = curr + 1
                elif target < i[curr]:
                    right = curr - 1
                else:
                    return True
        return False
