class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.nodes = defaultdict(list)
        
        for src, dest in prerequisites:
            self.nodes[src].append(dest)
            
        def DFS(node, visited):
            if visited[node] == 1:
                return True
            if visited[node] == -1:
                return False
            
            visited[node] = -1
            
            for vertex in self.nodes[node]:
                if not DFS(vertex, visited):
                    return False
                
            visited[node] = 1
            L.append(node)
            return True
        
        
        visited = [0 for _ in range(numCourses)]
        L = []
        
        for node in range(numCourses):
            if not DFS(node, visited):
                return []
            
        return L