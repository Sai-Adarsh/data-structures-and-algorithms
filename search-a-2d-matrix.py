class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            left = 0
            right = len(i) - 1
            while left <= right:
                curr = left + (right - left) // 2
                if i[curr] == target:
                    return True
                elif target > i[curr]:
                    left = curr + 1
                else:
                    right = curr - 1
        return False
