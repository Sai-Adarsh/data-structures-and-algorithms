# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return
        
        L = []
        while head:
            if not head:
                return
            L.append(head.val)
            head = head.next
    
        L[:] = L[:m - 1] + L[m - 1: n][::-1] + L[n:]
        first = ListNode(L[0])
        final = first
        
        for i in range(1, len(L)):
            node = ListNode(L[i])
            first.next = node
            first = node
        return final