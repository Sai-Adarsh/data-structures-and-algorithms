# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        q = [root]
        currRow = []
        allRows = []

        while q:
            currRow = []
            for _ in range(len(q)):
                node = q.pop(0)
                currRow.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            allRows.append(sum(currRow) / len(currRow))
        return allRows