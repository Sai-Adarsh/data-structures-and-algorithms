class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        n = numCourses
        graph = defaultdict(list)
        g = defaultdict(set)
        
        for x, y in prerequisites:
            graph[y].append(x)
            g[x].add(y)
            
            
        B = [x for x in range(n) if not g[x]]
        i = 0
        while i < len(B):
            y = B[i]
            i += 1
            for x in graph[y]:
                g[x].remove(y)
                if not g[x]:
                    B.append(x)
                    
        return B if len(B) == numCourses else []