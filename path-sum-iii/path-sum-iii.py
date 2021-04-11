# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        def DFS(root, prev_sum):
            if not root:
                return
            curr_sum = prev_sum + root.val
            if curr_sum - targetSum in prefix_sum:
                self.count += prefix_sum[curr_sum - targetSum]
            if curr_sum not in prefix_sum:
                prefix_sum[curr_sum] = 1
            else:
                prefix_sum[curr_sum] += 1
            DFS(root.left, curr_sum)
            DFS(root.right, curr_sum)
            prefix_sum[curr_sum] -= 1
            
        self.count = 0
        prefix_sum = {0: 1}
        DFS(root, 0)
        return self.count