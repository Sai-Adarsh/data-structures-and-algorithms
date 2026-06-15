# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while head and head.next:
            head.next.val, head.val = head.val, head.next.val
            head = head.next.next
        
        return temp