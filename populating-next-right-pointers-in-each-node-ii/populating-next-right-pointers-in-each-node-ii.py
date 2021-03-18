"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        tree = root
        from collections import deque
        q = deque([root])
        curr_level = []
        all_levels = []
        
        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                curr_level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            all_levels.append(curr_level)
        for level in all_levels:
            for j in range(len(level) - 1):
                if j == len(level) - 1:
                    level[j].next = None
                else:
                    level[j].next = level[j + 1]
                    
        return tree