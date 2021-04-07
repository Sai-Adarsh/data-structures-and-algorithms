# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        self.L = []
        
        while head:
            if not head:
                return
            self.L.append(head.val)
            head = head.next
        self.L.sort()
        
        first = ListNode(self.L[0])
        final = first
        
        for _ in range(1, len(self.L)):
            node = ListNode(self.L[_])
            first.next = node
            first = node
        return final