class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        if n == 1 or n==2:
            return [i for i in range(n)]
        
        self.nodes = defaultdict(list)
        
        for node, neighbor in edges:
            self.nodes[node].append(neighbor)
            self.nodes[neighbor].append(node)
        
        
        
        
        visited = [0 for _ in range(n)]
        q = collections.deque([])
        
        for node in range(n):
            if len(self.nodes[node]) == 1:
                visited[node] = 1
                q.append(node)
                
        level = 0
        while sum(visited) != n:
            for _ in range(len(q)):
                node = q.popleft()
                vertex = self.nodes[node].pop()
                self.nodes[vertex].remove(node)
                if len(self.nodes[vertex]) == 1:
                    q.append(vertex)
                    visited[vertex] = 1
                    
            level += 1
            
        return list(q)