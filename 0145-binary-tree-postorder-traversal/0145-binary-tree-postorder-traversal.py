# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.BFS(root, res)
        return res
    def BFS(self, root, res):
        if not root:
            return
        self.BFS(root.left, res)
        self.BFS(root.right, res)
        res.append(root.val)