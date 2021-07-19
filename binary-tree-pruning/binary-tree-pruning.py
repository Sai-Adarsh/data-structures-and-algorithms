# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        
        def DFS(root):
            if not root:
                return
            root.left = DFS(root.left)
            root.right = DFS(root.right)
            if root.val == 1:
                return root
            else:
                if not root.left and not root.right:
                    return
            return root
        root = DFS(root)
        return root
                