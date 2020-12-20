# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.L1 = []
        self.L2 = []
        
        def DFS(root, L):
            if not root:
                L.append(None)
                return
            L.append(root.val)
            DFS(root.left, L)
            DFS(root.right, L)
            return L
        return DFS(p, self.L1) == DFS(q, self.L2)
