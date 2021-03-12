# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        self.L = []
        while head:
            if not head:
                return
            self.L.append(head)
            head = head.next
        
        self.L[k - 1], self.L[len(self.L) - k] = self.L[len(self.L) - k], self.L[k - 1]
        
        first = ListNode(self.L[0].val)
        final = first
        
        for _ in range(1, len(self.L)):
            node = ListNode(self.L[_].val)
            first.next = node
            first = node
        return final