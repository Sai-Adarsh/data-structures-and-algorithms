# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        self.all_levels = {}
        
        def DFS(root, level, from_top):
            if not root:
                return
            if level not in self.all_levels:
                self.all_levels[level] = [from_top]
            else:
                self.all_levels[level].append(from_top)
            DFS(root.left, level + 1, from_top * 2)
            DFS(root.right, level + 1, from_top * 2 + 1)
            
        DFS(root, 0, 0)
        return max([max(each_level) - min(each_level) + 1 for each_level in self.all_levels.values()])