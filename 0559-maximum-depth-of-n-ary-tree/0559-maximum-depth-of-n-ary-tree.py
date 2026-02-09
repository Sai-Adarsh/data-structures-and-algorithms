"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = [root]
        currLevel = 0

        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                for eachChild in node.children:
                    q.append(eachChild)
            currLevel += 1

        return currLevel