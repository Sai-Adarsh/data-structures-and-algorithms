# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helperDFS(root, subRoot):
            if not subRoot and not root:
                return True
            if not subRoot or not root:
                return False
            if root.val != subRoot.val:
                return False
            left = helperDFS(root.left, subRoot.left)
            right = helperDFS(root.right, subRoot.right)
            return left and right


        self.ans = False
        def DFS(root):
            if not root:
                return
            if root.val == subRoot.val:
                if helperDFS(root, subRoot):
                    self.ans = True
            DFS(root.left)
            DFS(root.right)

        DFS(root)
        return self.ans

