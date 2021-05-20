# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return
        m = left
        n = right
        h, p = head, None
        
        for _ in range(m - 1):
            p = h
            h = h.next
            
        prev = p
        curr = h
        ahead = curr.next
        
        #we move prev and h
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