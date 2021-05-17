# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return
        
        while head:
            if not head:
                return
            if head.val == "LeetCode":
                return True
            head.val = "LeetCode"
            head = head.next
            
        return False