# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
            if not len(inorder):
                return
            root_val = preorder.pop(0)
            root_index = inorder.index(root_val)
            
            left = self.buildTree(preorder, inorder[:root_index])
            right = self.buildTree(preorder, inorder[root_index + 1:])
        
            root = TreeNode(root_val, left, right)
            
            return root