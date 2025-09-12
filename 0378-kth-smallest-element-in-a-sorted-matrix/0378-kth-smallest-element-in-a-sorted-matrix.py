class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        L = []
        heapq.heapify(L)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(L, matrix[i][j])
        
        for _ in range(k - 1):
            heapq.heappop(L)

        return heapq.heappop(L)