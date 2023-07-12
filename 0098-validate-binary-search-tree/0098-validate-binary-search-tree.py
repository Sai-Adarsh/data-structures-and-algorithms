# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.prevVal = None

        self.ans = True
        def DFS(root):
            if not root:
                return
            DFS(root.left)
            if self.prevVal != None:
                if root.val <= self.prevVal:
                    self.ans = False
                    return
            self.prevVal = root.val
            DFS(root.right)
        DFS(root)
        return self.ans