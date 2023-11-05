class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import numpy
        matrix[:] = [each[::-1] for each in numpy.transpose(matrix)]