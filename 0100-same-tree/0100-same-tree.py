# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def returnRes(p):
            resP = []
            q = [p]

            while q:
                for _ in range(len(q)):
                    node = q.pop(0)
                    if not node:
                        resP.append(None)
                        continue
                    resP.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            return resP
        return returnRes(p) == returnRes(q)