# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return
        
        root = head
        while root and root.next:
            if not root:
                return
            if root.val == root.next.val:
                root.next = root.next.next
            else:
                root = root.next
                
        return head