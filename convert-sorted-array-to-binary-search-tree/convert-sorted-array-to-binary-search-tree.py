# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        left = 0
        right = len(nums) - 1
        return self.helper(nums, left, right, None)
        
        
    def helper(self, nums, left, right, root):
        while left <= right:
            curr = left + (right - left) // 2
            root = TreeNode(nums[curr])
            root.left = self.helper(nums, left, curr - 1, root.left)
            root.right = self.helper(nums, curr + 1, right, root.right)
            return root