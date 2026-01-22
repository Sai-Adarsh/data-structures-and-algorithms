# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        forward = []
        reverse = []

        prev = None
        curr = head

        while curr:
            forward.append(curr.val)
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead

        while prev:
            reverse.append(prev.val)
            prev = prev.next

        return forward == reverse