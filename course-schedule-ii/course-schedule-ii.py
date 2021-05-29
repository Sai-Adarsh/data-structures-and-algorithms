class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        n = numCourses
        graph = defaultdict(list)
        g = defaultdict(set)
        
        
        for v, u in prerequisites:
            graph[u].append(v)
            g[v].add(u)
            
            
            
        B = [v for v in range(n) if not g[v]]
        
        i = 0
        while i < len(B):
            u = B[i]
            i += 1
            for v in graph[u]:
                g[v].remove(u)
                if not g[v]:
                    B.append(v)
                    
        return B if len(B) == n else []
        