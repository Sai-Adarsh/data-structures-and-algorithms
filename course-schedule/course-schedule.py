class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        n = numCourses
        graph = [[] for _ in range(n)]
        g = [0] * n
        for v, u in prerequisites:
            graph[u].append(v)
            g[v] += 1
        S = [ v for v in range(n) if g[v] == 0]
        while S:
            u = S.pop()
            for v in graph[u]:
                g[v] -= 1
                if g[v] == 0:
                    S.append(v)
        return not any(g)