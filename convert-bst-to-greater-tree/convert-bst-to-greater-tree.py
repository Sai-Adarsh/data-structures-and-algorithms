# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        tree = root
        self.L = []
        def DFS(tree):
            if not tree:
                return
            self.L.append(tree.val)
            DFS(tree.left)
            DFS(tree.right)
        DFS(tree)
        self.L.sort()

        def helper(val):
            is_there = bisect.bisect_left(self.L, val)
            return sum(self.L[is_there:])
        
        tree = root
        def DFS(tree):
            if not tree:
                return
            tree.val = helper(tree.val)
            DFS(tree.left)
            DFS(tree.right)
        DFS(tree)
        return root
