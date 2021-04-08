# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return
        
        count = 0
        root = head
        
        while root:
            if not root:
                return
            count += 1
            root = root.next
        
        n = count - n
        root = head
        count2 = 0
        if count == count - n:
            return root.next
        
        while root:
            if count2 + 1 == n:
                root.next = root.next.next
            count2 += 1
            root = root.next
        
        return head