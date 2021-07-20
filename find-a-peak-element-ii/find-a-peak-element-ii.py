class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        
        # loop through 2D
        # put legit neighbors in a list, check if mat[i][j] > max(legit_list), if so, return [i, j]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                legit_list = []
                if 0 <= i + 1 <= len(mat) - 1 and 0 <= j <= len(mat[0]) - 1:
                    legit_list.append(mat[i + 1][j])
                if 0 <= i - 1 <= len(mat) - 1 and 0 <= j <= len(mat[0]) - 1:
                    legit_list.append(mat[i - 1][j])
                if 0 <= i <= len(mat) - 1 and 0 <= j + 1 <= len(mat[0]) - 1:
                    legit_list.append(mat[i][j + 1])
                if 0 <= i <= len(mat) - 1 and 0 <= j - 1 <= len(mat[0]) - 1:
                    legit_list.append(mat[i][j - 1])
                if mat[i][j] > max(legit_list):
                    return [i, j]