import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        
    def push(self, matrixSum, indexes):
        heapq.heappush(self._queue, (matrixSum, indexes))
        
    def pop(self) -> tuple:
        return heapq.heappop(self._queue)

    
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        queue = PriorityQueue()
        
        m = len(mat)  # row
        n = len(mat[0]) # col
        
        smallestSum = sum(mat[i][0] for i in range(0, m))
        firstColIndexes = tuple([0 for _ in range(0, m)])
        queue.push(smallestSum, firstColIndexes)
        
        
        usedIndexes = set()
        usedIndexes.add(firstColIndexes)
        
        kCount = 0
        
        while 1:
            matSum, colIndexes = queue.pop()
            kCount += 1
            
            if kCount == k:
                return matSum

            for rowIndex, colIndex in enumerate(colIndexes):
                if colIndex < n - 1:
                    colIndexesCopy = list(colIndexes)
                    colIndexesCopy[rowIndex] += 1
                    colIndexesCopy = tuple(colIndexesCopy)
                    
                    if colIndexesCopy not in usedIndexes:
                        matSum = sum(mat[row][colIndexesCopy[row]] for row in range(0, m))
                        queue.push(matSum, colIndexesCopy)
                        usedIndexes.add(colIndexesCopy)