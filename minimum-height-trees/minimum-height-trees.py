class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1 or n == 1:
            return [i for i in range(n)]
        
        
        nodes = defaultdict(list)
        
        for node, neighbor in edges:
            nodes[node].append(neighbor)
            nodes[neighbor].append(node)
            
            
        q = collections.deque()
        visited = [0 for _ in range(n)]
        
        for node in range(n):
            if len(nodes[node]) == 1:
                q.append(node) # leaf nodes
                visited[node] = 1
                
                
        level = 0
        while sum(visited) != n:
            for _ in range(len(q)):
                node = q.popleft()
                vertex = nodes[node].pop()
                nodes[vertex].remove(node)
                if len(nodes[vertex]) == 1:
                    visited[vertex] = 1
                    q.append(vertex)
                    
            level += 1
            
        return list(q)