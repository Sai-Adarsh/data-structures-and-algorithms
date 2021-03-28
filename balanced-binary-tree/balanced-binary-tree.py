# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        self.ans = True
        def DFS(root):
            if not root:
                return 0
            
            left = DFS(root.left)
            right = DFS(root.right)
            if abs(left - right) > 1:
                self.ans = False
            return max(left, right) + 1
        
        DFS(root)
        return self.ans