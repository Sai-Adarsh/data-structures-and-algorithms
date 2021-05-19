# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if not head:
            return
        
        h, p = head, None
        
        for _ in range(m - 1):
            p = h
            h = h.next
            
        curr = h
        prev = p
        ahead = curr.next
        
        for _ in range(n - m + 1):
            h.next = prev
            prev = h
            h = ahead
            
            if ahead:
                ahead = ahead.next
                
        if p:
            p.next = prev
        else:
            head = prev
            
        curr.next = h
        return head