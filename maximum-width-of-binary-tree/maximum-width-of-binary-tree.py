# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        self.level_dict = {}
        def DFS(root, level, from_top):
            if root:
                if level not in self.level_dict:
                    self.level_dict[level] = [from_top]
                else:
                    self.level_dict[level].append(from_top)
                DFS(root.left, level + 1, from_top * 2)
                DFS(root.right, level + 1, (from_top * 2) + 1)
        
        
        DFS(root, 0, 0)
        return max([max(self.level_dict[level]) - min(self.level_dict[level]) + 1 for level in self.level_dict])