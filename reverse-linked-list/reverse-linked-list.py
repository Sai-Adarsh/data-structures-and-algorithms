# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        self.L = []
        while head:
            if not head:
                return
            self.L.append(head.val)
            head = head.next
        self.L[:] = self.L[::-1]
        first = ListNode(self.L[0])
        final = first
        
        for _ in range(1, len(self.L)):
            node = ListNode(self.L[_])
            first.next = node
            first = node
        
        return final
        