# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = [root]
        currRow = 0
        sawLeaf = False

        while q:
            for i in range(len(q)):
                node = q.pop(0)
                if not node.left and not node.right:
                    sawLeaf = True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            currRow += 1
            if sawLeaf:
                return currRow
        return currRow