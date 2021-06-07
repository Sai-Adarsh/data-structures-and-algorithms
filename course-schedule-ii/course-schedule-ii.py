class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
        def DFS(node, visited):
            if visited[node] == -1:
                return False

            if visited[node] == 1:
                return True
            
            visited[node] = -1

            for course in self.nodes[node]:
                if not DFS(course, visited):
                    return False

            visited[node] = 1
            L.append(node)
            return True
        
        visited = [0] * numCourses
        
        self.nodes = defaultdict(list)
        for node, neighbors in prerequisites:
            self.nodes[node].append(neighbors)

        L = []
        for node in range(numCourses):
            if not DFS(node, visited):
                return []

        return L