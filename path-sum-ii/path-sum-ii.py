# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        def DFS(root, s):
            if not root:
                return
            DFS(root.left, s + [root.val])
            DFS(root.right, s + [root.val])
            if not root.left and not root.right:
                if sum(s + [root.val]) == targetSum:
                    self.L.append(s + [root.val])
        
        self.L = []
        s = []
        DFS(root, s)
        return self.L
        
        