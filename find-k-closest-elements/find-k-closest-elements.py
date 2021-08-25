class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        L = [(i, abs(i - x)) for i in arr]
        L.sort(key = lambda x: x[1])
        return sorted([L.pop(0)[0] for _ in range(k)])