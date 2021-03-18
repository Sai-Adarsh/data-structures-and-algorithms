# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        from collections import deque
        q = deque([root])
        curr_level = []
        all_levels = []
        met = False
        while q:
            curr_level = []
            
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                if not node.left and not node.right:
                    met = True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            all_levels.append(curr_level)
            if met == True:
                return len(all_levels)