# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        L = []
        
        while head:
            if not head:
                return
            L.append(head.val)
            head = head.next
        i = 0
        while i <= len(L) - k:
            L[i:i + k] = L[i:i + k][::-1]
            i += k
                        
        first = ListNode(L[0])
        final = first
        
        for _ in range(1, len(L)):
            node = ListNode(L[_])
            first.next = node
            first = node
        return final