# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        one = ""
        two = ""
        
        while l1:
            if not l1:
                break
            one += str(l1.val)
            l1 = l1.next
            
        while l2:
            if not l2:
                break
            two += str(l2.val)
            l2 = l2.next
            
        one = int(one[::-1])
        two = int(two[::-1])
        
        one = one + two
        one = str(one)
        one = one[::-1]
        
        one = [i for i in one]
        
        
        if not one:
            return 0
        
        first = ListNode(int(one[0]))
        final = first
        
        for _ in range(1, len(one)):
            node = ListNode(int(one[_]))
            first.next = node
            first = node
            
        return final