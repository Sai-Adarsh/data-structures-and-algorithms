class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        nodes = defaultdict(list)

        for node, neighbors in adjacentPairs:
            nodes[neighbors].append(node)
            nodes[node].append(neighbors)

        def DFS(nodes, node, visited, res):
            visited.add(node)
            res.append(node)
            for vertex in nodes[node]:
                if vertex not in visited:
                    DFS(nodes, vertex, visited, res)
            return


        visited = set()
        res = []
        for node in nodes:
            if len(nodes[node]) == 1:
                start = node
                
        DFS(nodes, start, visited, res)

        return(res)