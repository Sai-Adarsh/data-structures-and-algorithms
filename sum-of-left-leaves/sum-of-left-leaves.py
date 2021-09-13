# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        self.res = 0
        def DFS(root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                self.res += root.left.val
            DFS(root.left)
            DFS(root.right)
        DFS(root)
        return self.res