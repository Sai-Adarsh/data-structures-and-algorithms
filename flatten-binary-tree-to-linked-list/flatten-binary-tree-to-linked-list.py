# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.L = []
        def DFS(root):
            if not root:
                return
            self.L.append(root)
            DFS(root.left)
            DFS(root.right)
            
        DFS(root)
        for i in range(len(self.L)):
            if i == len(self.L) - 1:
                self.L[i].left, self.L[i].right = None, None
            else:
                self.L[i].left, self.L[i].right = None, self.L[i + 1]
            