class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        nodes = defaultdict(list)
        
        for node, neighbors in prerequisites:
            nodes[node].append(neighbors)
            
        def DFS(node, visited):
            if visited[node] == -1:
                return False
            
            if visited[node] == 1:
                return True
            
            visited[node] = -1
            
            for vertex in nodes[node]:
                if not DFS(vertex, visited):
                    return False
            
            
            visited[node] = 1
            L.append(node)
            return True
            
        visited = [0] * numCourses 
        L = []
        
        for node in range(numCourses):
            if not DFS(node, visited):
                return []
            
        return L