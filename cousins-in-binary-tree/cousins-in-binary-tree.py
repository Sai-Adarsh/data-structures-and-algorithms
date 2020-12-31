# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.xParent = None
        self.xDepth = -1
        self.yParent = None
        self.yDepth = -2
        
        def DFS(root, parent, x, y, depth):
            if root is None:
                return
            if root.val == x:
                self.xParent = parent
                self.xDepth = depth
            elif root.val == y:
                self.yParent = parent
                self.yDepth = depth
            else:
                DFS(root.left, root, x, y, depth + 1)
                DFS(root.right, root, x, y, depth + 1)
        DFS(root, None, x, y, 0)
        return self.xDepth == self.yDepth and self.xParent != self.yParent
