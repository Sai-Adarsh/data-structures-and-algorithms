# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return
        
        self.L = []
        while head:
            if not head:
                return
            if head.val != val:
                self.L.append(head.val)
            head = head.next
        if not self.L:
            return
        first = ListNode(self.L[0])
        final = first
        
        for _ in range(1, len(self.L)):
            node = ListNode(self.L[_])
            first.next = node
            first = node
        
        return final
            