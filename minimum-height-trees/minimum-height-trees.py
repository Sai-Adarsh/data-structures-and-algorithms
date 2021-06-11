class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1 or n == 2:
            return [_ for _ in range(n)]
        
        # undirected graph
        nodes = defaultdict(list)
        for node, neighbor in edges:
            nodes[node].append(neighbor)
            nodes[neighbor].append(node)
            
            
        visited = [0 for _ in range(n)]
        q = collections.deque()
        
        for i in range(n):
            # append leaf nodes to q
            if len(nodes[i]) == 1:
                q.append(i)
                visited[i] = 1
                
        level = 0
        while sum(visited) != n:
            for _ in range(len(q)):
                # 0, 2, 3
                # 0: [1]
                # 2: [1]
                # 3: [1]
                node = q.popleft()
                # vertex = 1
                vertex = nodes[node].pop()
                # 1: [0, 2, 3]
                # 1: [2, 3]
                # 1: [3]
                nodes[vertex].remove(node)
                if len(nodes[vertex]) == 1:
                    q.append(vertex)
                    visited[vertex] = 1
                    
                    
            level += 1
        return list(q)