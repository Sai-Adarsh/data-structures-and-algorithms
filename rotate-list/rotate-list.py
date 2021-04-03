# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        
        from collections import deque
        L = deque([])
        
        root = head
        while root:
            if not root:
                return
            L.append(root)
            root = root.next
            
        for _ in range(k % len(L)):
            L.appendleft(L.pop())
            
        root = head = L.popleft()
        
        while L:
            root.next = L.popleft()
            root = root.next
        
        root.next = None
        return head