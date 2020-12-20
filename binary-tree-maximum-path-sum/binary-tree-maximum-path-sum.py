# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        import sys
        self.result = -sys.maxsize - 1
        
        def DFS(root):
            if not root:
                return 0
            left = DFS(root.left)
            right = DFS(root.right)
            ms = max(max(left, right) + root.val, root.val)
            m21 = max(ms, left + right + root.val)
            self.result = max(m21, self.result)
            return ms
        DFS(root)
        return self.result
