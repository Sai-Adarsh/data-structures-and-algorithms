# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        prev = None
        curr = head
        ahead = head.next
        while curr:
            if not head:
                return
            curr.next = prev
            prev = curr
            curr = ahead
            if ahead:
                ahead = ahead.next
        return prev
