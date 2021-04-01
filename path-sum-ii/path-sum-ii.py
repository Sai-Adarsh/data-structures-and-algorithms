# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        
        def DFS(root, s, L):
            if not root:
                return
            if not root.left and not root.right and sum(s + [root.val]) == targetSum:
                L.append(s + [root.val])
            DFS(root.left, s + [root.val], L)
            DFS(root.right, s + [root.val], L)
            
        L = []
        s = []
        DFS(root, s, L)
        return(L)