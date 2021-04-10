# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        
        self.ans = None
        def DFS(root):
            if not root:
                return
            if root.val == val:
                self.ans = root
            DFS(root.left)
            DFS(root.right)
        DFS(root)
        return self.ans