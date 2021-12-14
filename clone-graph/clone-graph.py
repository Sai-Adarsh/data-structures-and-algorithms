"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        
        hashMap = {None: None}
        
        def DFS(node, hashMap):
            if not node:
                return
            if node in hashMap:
                return hashMap[node]
            hashMap[node] = Node(node.val)
            for eachNode in node.neighbors:
                hashMap[node].neighbors.append(DFS(eachNode, hashMap))
                
            return hashMap[node]
        
        return DFS(node, hashMap)
                