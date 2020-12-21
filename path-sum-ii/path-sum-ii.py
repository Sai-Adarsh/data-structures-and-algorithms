# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        L = []
        from numpy import sum as summation
        def DFS(root, s):
            if not root:
                return
            if not root.left and not root.right and summation(s + [root.val]) == sum:
                L.append(s + [root.val])
            DFS(root.left, s + [root.val])
            DFS(root.right, s + [root.val])
        DFS(root, [])
        return L
