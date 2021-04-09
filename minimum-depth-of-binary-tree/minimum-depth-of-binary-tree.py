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
        all_levels = []
        curr_level = []
        
        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                if not node.left and not node.right:
                    return len(all_levels) + 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            all_levels.append(curr_level)
        return len(all_levels) + 1