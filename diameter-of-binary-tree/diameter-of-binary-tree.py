# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        import sys
        self.res = 1
        def DFS(root):
            if not root:
                return 0
            left = DFS(root.left)
            right = DFS(root.right)
            self.res = max(self.res, left + right + 1)
            return max(left, right) + 1
        DFS(root)
        return self.res - 1