class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        answer = []
        visited = []
        dest = len(graph)-1
        
        def DFS(node):
            if node == dest:
                answer.append(visited.copy())
                return
            else:
                for i in graph[node]:
                    visited.append(i)
                    DFS(i)
                    visited.pop()
                    
        visited.append(0)
        DFS(0)
        return answer