class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        
        graph = defaultdict(list)
        
        n = len(isConnected)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
                    
        visit = [False for _ in range(n)]
        
        def DFS(node):
            for vertex in graph[node]:
                if visit[vertex] == False:
                    visit[vertex] = True
                    DFS(vertex)
                    
        count = 0
        for i in range(n):
            if visit[i] == False:
                count += 1
                visit[i] = True
                DFS(i)
                
        return count