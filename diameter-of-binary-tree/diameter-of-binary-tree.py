# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def DFS(root):
            if not root:
                return 0
            L = DFS(root.left)
            R = DFS(root.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1
        
        DFS(root)
        return self.ans - 1
