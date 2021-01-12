class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        from numpy import transpose
        matrix[:] = [i[::-1] for i in transpose(matrix)]
