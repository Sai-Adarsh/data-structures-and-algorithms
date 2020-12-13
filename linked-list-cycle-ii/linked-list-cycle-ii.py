# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return
        while head:
            if head.val == "LeetCode":
                return head
            head.val = "LeetCode"
            head = head.next
