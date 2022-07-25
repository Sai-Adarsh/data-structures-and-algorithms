class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        self.nodes = defaultdict(list)
        
        for dest, src in prerequisites:
            self.nodes[src].append(dest)
            
            
        def DFS(node, visited):
            if node not in self.nodes:
                return True
            if node in visited:
                return True
            if node in stack:
                return False
            stack.add(node)
            for children in self.nodes[node]:
                if not DFS(children, visited):
                    return False
            visited.add(node)
            return True
            
        visited = set()
        for node in range(numCourses):
            stack = set()
            if not DFS(node, visited):
                return False
        return True