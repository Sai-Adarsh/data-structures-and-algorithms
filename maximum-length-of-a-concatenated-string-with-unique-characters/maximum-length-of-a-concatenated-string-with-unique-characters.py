class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        visited = set()
        self.res = 0
        
        def backTracking(curr_path, start):
            if start == len(arr):
                if curr_path not in visited:
                    visited.add(curr_path)
                    self.res = max(self.res, len(curr_path))
                return
            
            if curr_path not in visited:
                visited.add(curr_path)
                self.res = max(self.res, len(curr_path))
            
            
            for i in range(start, len(arr)):
                if len(curr_path + arr[i]) == len(set(curr_path + arr[i])):
                    backTracking(curr_path + arr[i], i + 1)
                
        
        L = backTracking("", 0)
        return self.res