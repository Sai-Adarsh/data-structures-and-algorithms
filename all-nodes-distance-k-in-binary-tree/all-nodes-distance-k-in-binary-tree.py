# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
        def add_parent(root, prev_node):
            if not root:
                return
            root.parent = prev_node
            add_parent(root.left, root)
            add_parent(root.right, root)
            
        add_parent(root, None)
        
        
        res = []
        visited = set()
        
        def DFS(root, distance):
            if not root:
                return
            if root.val not in visited:
                visited.add(root.val)
                if distance == k:
                    res.append(root.val)
                DFS(root.parent, distance + 1)
                DFS(root.left, distance + 1)
                DFS(root.right, distance + 1)
                
                
        DFS(target, 0)
        return res