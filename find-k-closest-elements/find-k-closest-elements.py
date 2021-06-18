class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        L = [(abs(i - x), i) for i in arr]
        
        L.sort(key = lambda x: x[0])
        return sorted([L.pop(0)[1] for _ in range(k)])