# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        import heapq
        self.L = []
        heapq.heapify(self.L)
        def DFS(root):
            if not root:
                return
            self.L.append(root.val)
            DFS(root.left)
            DFS(root.right)
        
        DFS(root)
        return heapq.nsmallest(k, self.L)[-1]
        