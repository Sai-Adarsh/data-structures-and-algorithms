# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        
        L = []
        prefix_sum = [0]
        
        def DFS(root):
            if not root:
                return
            DFS(root.left)
            L.append(root.val)
            prefix_sum.append(prefix_sum[-1] + root.val)
            DFS(root.right)
            
        DFS(root)
        one = bisect.bisect_left(L, low)
        two = bisect.bisect_left(L, high)
        
        flag = False
        if one < 0:
            one = 0
        if two >= len(L) - 1:
            flag = True
            two = len(L) - 1
        
        return prefix_sum[two + 1] - prefix_sum[one]