# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        return self.backTracking(nums, 0, len(nums) - 1, TreeNode())
    
    def backTracking(self, nums, left, right, root):
        while left <= right:
            curr = left + (right - left) // 2
            root = TreeNode(nums[curr])
            root.left = self.backTracking(nums, left, curr - 1, root.left)
            root.right = self.backTracking(nums, curr + 1, right, root.right)
            return root
    
    