# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        odd = []
        even = []
        count = 0
        while head:
            if not head:
                return
            if count % 2 == 0:
                even.append(head.val)
            else:
                odd.append(head.val)
            count += 1
            head = head.next
        
        odd[:] = even + odd
        first = ListNode(odd[0])
        final = first
        
        for _ in range(1, len(odd)):
            node = ListNode(odd[_])
            first.next = node
            first = node
        return final