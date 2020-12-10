class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        seen = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                seen.append(matrix[i][j])
                
        seen.sort()
        import heapq
        heapq.heapify(seen)
        return heapq.nsmallest(k, seen)[-1]
