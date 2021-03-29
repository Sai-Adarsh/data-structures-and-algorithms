# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        
        def helper(root, L):
            if not root:
                L.append(None)
                return
            L.append(root.val)
            helper(root.left, L)
            helper(root.right, L)
            if not root.left and not root.right:
                L.append(None)
                L.append(None)
            return L
        
        def DFS(root):
            if not root:
                return
            if root.val == self.sub_tree:
                if helper(root, self.s1) == helper(t, self.t1):
                    self.ans = True
                else:
                    self.s1 = []
                    self.t1 = []
            DFS(root.left)
            DFS(root.right)
            
        self.s1 = []
        self.t1 = []
        self.ans = False
        self.sub_tree = t.val
        DFS(s)
        return self.ans