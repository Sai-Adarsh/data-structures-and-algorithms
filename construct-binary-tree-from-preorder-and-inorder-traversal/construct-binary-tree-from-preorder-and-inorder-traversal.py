# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder or len(inorder) == 0:
            return
        
        root_val = preorder .pop(0)
        root_index = inorder.index(root_val)
        
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index + 1:])
        return root