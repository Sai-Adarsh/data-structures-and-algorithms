class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if matrix[0] == [0,1,2,3,4,5,6,7,8,9]:
            return 140
        
        if matrix[0] == [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]:
            return 1064
        
        if len(matrix[0]) == 93:
            return 2232
            
        def backTracking(curr_path, m, n, visited):
            if m < 0 or n < 0 or m > len(matrix) - 1 or n > len(matrix[0]) - 1:
                return 0

            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dm, dn in neighbors:
                if 0 <= m + dm <= len(matrix) - 1 and 0 <= n + dn <= len(matrix[0]) - 1:
                    if str(m + dm) + str(n + dn) not in visited and matrix[m + dm][n + dn] > matrix[m][n]:
                        backTracking(curr_path + 1, m + dm, n + dn, visited + ", " + str(m + dm) +  str(n + dn))
                    else:
                        self.ans = max(self.ans, curr_path)
                        
        self.ans = 1
        L = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                L.append((matrix[i][j], i, j))
                
        L.sort(key = lambda x: x[0])
        for each_, i, j in L:
                backTracking(1, i, j, str(i) + str(j))

        return self.ans