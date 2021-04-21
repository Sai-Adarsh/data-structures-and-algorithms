"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        from collections import deque
        q = deque([root])
        curr_level = []
        all_levels = []
        
        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node.val)
                for each_root in node.children:
                    if each_root:
                        q.append(each_root)
                        
            all_levels.append(curr_level)
        return all_levels
            