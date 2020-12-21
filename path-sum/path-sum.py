# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        
        L = []
        s = 0
        def DFS(root, L, s):
            if not root:
                return 
            s += root.val
            DFS(root.left, L, s)
            DFS(root.right, L, s)
            if not root.left and not root.right:
                L.append(s)
        DFS(root, L, s)
        return sum in L
                
                
