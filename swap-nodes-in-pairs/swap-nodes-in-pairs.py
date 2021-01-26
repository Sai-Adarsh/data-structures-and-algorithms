# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        odd = []
        even = []
        counter = 0
        while head:
            if not head:
                return
            if counter % 2 == 0:
                even.append(head.val)
            else:
                odd.append(head.val)
            counter += 1
            head = head.next
        L = []
        for i in range(max(len(odd), len(even))):
            if i < len(odd):
                L.append(odd[i])
            if i < len(even):
                L.append(even[i])
        first = ListNode(L[0])
        final = first
        for i in range(1, len(L)):
            node = ListNode(L[i])
            first.next = node
            first = node
        return final
