# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.L = []
        
        def DFS(root):
            if not root:
                return
            self.L.append(root.val)
            DFS(root.left)
            DFS(root.right)
        DFS(root)
        
        return sum([i for i in self.L if i >= low and i <= high])
