# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        left = 0
        right = len(nums) - 1
        return self.helper(left, right, nums, None)
    
​
    def helper(self, left, right, nums, root):
        while left <= right:
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = self.helper(left, mid - 1, nums, root.left)
            root.right = self.helper(mid + 1, right, nums, root.right)
            return root
​
