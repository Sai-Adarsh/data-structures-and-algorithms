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
        oldCopy = {None: None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            oldCopy[curr] = copy
            curr = curr.next
            
        curr = head
        while curr:
            copy = oldCopy[curr]
            copy.next = oldCopy[curr.next]
            copy.random = oldCopy[curr.random]
            curr = curr.next 
        return oldCopy[head]