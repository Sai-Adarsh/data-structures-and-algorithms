class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        
        arr = [0, 1]
        while True:
            if arr[-1] >= k:
                break
            else:
                arr.append(arr[-1] + arr[-2])
                
                
        count = 0
        for i in range(len(arr) -1, -1, -1):
            if arr[i] <= k:
                k -= arr[i]
                count += 1
            if k == 0:
                return count