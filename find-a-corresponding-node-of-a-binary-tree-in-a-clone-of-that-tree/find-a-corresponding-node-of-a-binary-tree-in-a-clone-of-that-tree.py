# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.tree_container = TreeNode(None)
        
        def DFS(original, cloned, target):
            if not original or not cloned:
                return
            if original.val == target.val:
                self.tree_container = cloned
            DFS(original.left, cloned.left, target)
            DFS(original.right, cloned.right, target)
        DFS(original, cloned, target)
        return self.tree_container
