# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        q = [root]
        currLevel = []
        allLevels = []

        while q:
            currLevel = []
            for _ in range(len(q)):
                node = q.pop(0)
                currLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            allLevels.append(currLevel)

        return allLevels