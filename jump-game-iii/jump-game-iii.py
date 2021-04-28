class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        
        return self.backTracking(arr, start, set())
    
    def backTracking(self, arr, start, visited):
        # our constraints
        if start < 0 or start > len(arr) - 1 or start in visited:
            return False
        
        
        # our goal
        # base case
        if arr[start] == 0:
            return True
        
        # our choice
        # recursive case
        visited.add(start)
        return self.backTracking(arr, start + arr[start], visited) or self.backTracking(arr, start - arr[start], visited)
    
        