# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        L = []
        curr = head
        while curr:
            if not curr:
                return
            L.append(curr.val)
            curr = curr.next
        print(L)
        del L[len(L) - n]
        
        if not L:
            return
        first = ListNode(L[0])
        final = first
        
        for i in range(1, len(L)):
            node = ListNode(L[i])
            first.next = node
            first = node
        return final
