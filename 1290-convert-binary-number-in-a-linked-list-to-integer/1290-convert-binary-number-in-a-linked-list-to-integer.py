# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:

        resString = ""
        while head:
            if not head:
                return
            resString += str(head.val)
            head = head.next

        return int(resString, 2)