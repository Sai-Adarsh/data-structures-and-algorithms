"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.L = []
        
        def DFS(root):
            if not root:
                return
            self.L.append(root.val)
            for i in root.children:
                DFS(i)
            
        DFS(root)
        return self.L
