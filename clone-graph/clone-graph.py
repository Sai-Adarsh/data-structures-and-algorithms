"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloned = {}
        def DFS(node):
            if not node:
                return node
            elif node.val in cloned:
                return cloned[node.val]
            else:
                ans = Node(node.val)
                cloned[node.val] = ans
                for n in node.neighbors:
                    ans.neighbors.append(DFS(n))
                return ans
        
        return DFS(node)