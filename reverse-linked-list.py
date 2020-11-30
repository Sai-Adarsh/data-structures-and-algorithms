# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        ahead = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = ahead
            if ahead:
                ahead = ahead.next
        return prev
