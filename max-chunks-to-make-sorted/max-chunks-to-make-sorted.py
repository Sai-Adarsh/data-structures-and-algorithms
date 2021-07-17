class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        
        def canBeChunked(i, j):
            temp = arr[i : j + 1]
            count = 0
            for k in range(len(temp)):
                if temp[k] >= i and temp[k] <= j:
                    count += 1
            return count == j - i + 1
                    
        
        N = len(arr)
        i = 0
        res = 0
        while i < N:
            for j in range(i, N):
                if canBeChunked(i, j):
                    break
            i = j + 1
            res += 1
            
        return res