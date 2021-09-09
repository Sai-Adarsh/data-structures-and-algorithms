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
        is_dups = set()
        
        while root and root.next:
            if not root:
                return
            if root.val == root.next.val:
                is_dups.add(root.val)
                root.next = root.next.next
            else:
                root = root.next
                
        root = head
        
        if not root:
            return
        
        while True:
            if not root:
                break
            if root.val in is_dups:
                root = root.next
            else:
                break
        
        if not root:
            return
        
        head = root
        
        while root and root.next:
            if not root:
                return
            if root.next.val in is_dups:
                root.next = root.next.next
            else:
                root = root.next
        
        return head