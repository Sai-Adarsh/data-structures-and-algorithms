class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        self.nodes = defaultdict(list)
        
        for src, dest in prerequisites:
            self.nodes[src].append(dest)
            
        visited = [0 for _ in range(numCourses)]
        
        
        def DFS(node, visited):
            if visited[node] == 1:
                return True
            if visited[node] == -1:
                return False
            visited[node] = -1
            for children in self.nodes[node]:
                if not DFS(children, visited):
                    return False
            visited[node] = 1
            L.append(node)
            return True
        
        
        L = []
        for node in range(numCourses):
            if not DFS(node, visited):
                return []
            
        return L