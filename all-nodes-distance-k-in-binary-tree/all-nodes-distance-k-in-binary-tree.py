# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        def add_parent(node, parent = None):
            if not node:
                return
            node.parent = parent
            add_parent(node.left, node)
            add_parent(node.right, node)
    
        root = add_parent(root)
        res = []
        visited = set()
        
        def DFS(root, depth = 0):
            if not root:
                return
            if root.val not in visited:
                visited.add(root.val)
                if K == depth:
                    res.append(root.val)
                DFS(root.parent, depth + 1)
                DFS(root.left, depth + 1)
                DFS(root.right, depth + 1)
            return
        DFS(target)
        return res