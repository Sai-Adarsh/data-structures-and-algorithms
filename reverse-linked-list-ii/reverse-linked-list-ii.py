# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        if not head:
            return
        
        L = []
        while head:
            if not head:
                return
            L.append(head.val)
            head = head.next
                
        L[:] = L[:left - 1] + L[left - 1: right][::-1] +  L[right:]
        
        first = ListNode(L[0])
        final = first
        
        for _ in range(1, len(L)):
            node = ListNode(L[_])
            first.next = node
            first = node
            
        return final