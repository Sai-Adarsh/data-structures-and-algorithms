# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        if not root1 and not root2:
            return
        self.L = []
        def DFS(root):
            if not root:
                return
            self.L.append(root.val)
            DFS(root.left)
            DFS(root.right)
        if root1:
            DFS(root1)
        if root2:
            DFS(root2)
        return sorted(self.L)
        
