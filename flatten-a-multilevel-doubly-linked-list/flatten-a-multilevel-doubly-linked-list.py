"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
​
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        root = head
        self.L = []
        def doubly(head):
            if not head:
                return head
            self.L.append(head.val)
            doubly(head.child)
            doubly(head.next)
        doubly(head)
        first = Node(self.L[0])
        first.prev = None
        final = first
        for i in range(1, len(self.L)):
            node = Node(self.L[i])
            node.prev = first
