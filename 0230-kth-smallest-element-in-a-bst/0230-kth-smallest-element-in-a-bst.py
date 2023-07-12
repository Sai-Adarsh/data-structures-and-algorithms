# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        L = []
        heapq.heapify(L)

        def DFS(root):
            if not root:
                return
            DFS(root.left)
            heapq.heappush(L, root.val)
            DFS(root.right)
        DFS(root)
        return heapq.nsmallest(k, L).pop()