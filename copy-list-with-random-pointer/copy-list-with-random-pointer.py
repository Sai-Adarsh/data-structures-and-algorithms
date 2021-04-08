"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        
        hash_map = {None: None}
        
        root = head
        while root:
            if not root:
                return
            copy = Node(root.val)
            hash_map[root] = copy
            root = root.next
            
        root = head
        while root:
            node = hash_map[root]
            node.next = hash_map[root.next]
            node.random = hash_map[root.random]
            root = root.next
        return hash_map[head]