class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        return self.backTracking(arr, set(), start)
    
        
    def backTracking(self, arr, curr_path, start):
        if start < 0 or start > len(arr) - 1 or start in curr_path:
            return False
    
        if arr[start] == 0:
            return True
        
        
        curr_path.add(start)
        return self.backTracking(arr, curr_path, start + arr[start]) or self.backTracking(arr, curr_path, start - arr[start])