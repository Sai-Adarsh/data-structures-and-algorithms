# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        
        def DFS(root):
            if not root:
                return 0, 0
            left, right = DFS(root.left), DFS(root.right)
            vTakeRoot = root.val + left[1] + right[1]
            vNotTakeRoot = max(left) + max(right)
            return vTakeRoot, vNotTakeRoot
        
        return max(DFS(root))