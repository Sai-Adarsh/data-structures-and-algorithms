# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        from collections import deque
        q = deque([root])
        curr_level = []
        all_levels = []
        
        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            all_levels.append(curr_level)
        for i in range(len(all_levels)):
            if i % 2 == 0:
                for x in all_levels[i]:
                    if x % 2 == 0:
                        return False
                for x in range(len(all_levels[i]) - 1):
                    if all_levels[i][x] >= all_levels[i][x + 1]:
                        return False
            else:
                for x in all_levels[i]:
                    if x % 2 != 0:
                        return False
                for x in range(len(all_levels[i]) - 1):
                    if all_levels[i][x] <= all_levels[i][x + 1]:
                        return False
        return True
