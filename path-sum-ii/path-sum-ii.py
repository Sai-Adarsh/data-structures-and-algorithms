# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        L = []
        s = []
        def DFS(root, L, s):
            if not root:
                return
            if not root.left and not root.right and sum(s + [root.val]) == targetSum:
                L.append(s + [root.val])
            DFS(root.left, L, s + [root.val])
            DFS(root.right, L, s + [root.val])
        DFS(root, L, s)
        return L