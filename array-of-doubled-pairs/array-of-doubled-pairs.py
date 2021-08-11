class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        
        L = collections.Counter(arr)
        
        for i in sorted(arr, key = abs):
            if L[i] == 0:
                continue
            if L[2 * i] == 0:
                return False
            L[i] -= 1
            L[2 * i] -= 1
            
        return True