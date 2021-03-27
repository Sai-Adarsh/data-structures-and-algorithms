# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        self.L = []
        def DFS(root):
            if not root:
                return
            DFS(root.left)
            self.L.append(root.val)
            DFS(root.right)
            
        DFS(root)
        for i in range(len(self.L) - 1):
            if self.L[i] >= self.L[i + 1]:
                return False
        return True