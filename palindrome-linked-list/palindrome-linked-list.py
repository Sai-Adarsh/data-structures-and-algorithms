# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return
        L = []
        
        while head:
            if not head:
                return
            
            L.append(head.val)
            head = head.next
        
        return L == L[::-1]