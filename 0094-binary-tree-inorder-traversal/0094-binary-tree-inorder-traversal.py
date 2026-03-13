# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        self.BFS(root, res)
        return res
    def BFS(self, root, res):
        if not root:
            return
        self.BFS(root.left, res)
        res.append(root.val)
        self.BFS(root.right, res)