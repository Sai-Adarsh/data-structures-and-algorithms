class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        from collections import deque
        L = [(abs(i - x), i) for i in arr]
        L.sort(key = lambda x: (x[0], x[1]))
        L = deque(L)
        res = []
        for i in range(k):
            res.append(L.popleft()[1])
        return sorted(res)