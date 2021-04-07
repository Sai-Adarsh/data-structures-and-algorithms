# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        from collections import deque
        self.L = deque([])
        while head:
            if not head:
                return
            self.L.append(head)
            head = head.next
            
        root = head = self.L.popleft()
        root.next = None
        while self.L:
            if self.L:
                node = self.L.pop()
                node.next = None
                root.next = node
                root = node
            if self.L:
                node = self.L.popleft()
                node.next = None
                root.next = node
                root = node
        root.next = None
        return head