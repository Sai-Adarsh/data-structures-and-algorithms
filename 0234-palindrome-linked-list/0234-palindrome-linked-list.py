# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse, original = [], []

        if not head:
            return True

        root = head
        while root:
            original.append(root.val)
            root = root.next

        root = head
        prev = None
        curr = head
        ahead = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = ahead
            if ahead:
                ahead = ahead.next

        while prev:
            reverse.append(prev.val)
            prev = prev.next

        return original == reverse