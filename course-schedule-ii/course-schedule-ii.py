class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # detect cycle in directed graph
        nodes = defaultdict(list)
        
        for node, neighbor in prerequisites:
            nodes[node].append(neighbor)
            
        
        def DFS(node, visited, stack):
            if visited[node] == 1:
                return True
            if visited[node] == -1:
                return False
            
            visited[node] = -1
            
            for vertex in nodes[node]:
                if not DFS(vertex, visited, stack):
                    return False
            
            
            visited[node] = 1
            L.append(node)
            return True
        
        
        visited = [0 for _ in range(numCourses)]
        L = []
        
        for node in range(numCourses):
            stack = []
            if not DFS(node, visited, stack):
                return []
            
        return L