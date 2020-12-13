# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
​
        while head and head.val == val:
            head = head.next
        ll = head
        while ll and ll.next:
            if ll.next.val == val:
                ll.next = ll.next.next
            else:
                ll = ll.next
        return head
