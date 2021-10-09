# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # traverse and find the number
        # reverse the numbers
        # add the numbers
        # reverse the number
        # form a new ll
        one = []
        two = []
        
        if l1:
            while l1:
                if not l1:
                    return
                one.append(str(l1.val))
                l1 = l1.next
                
        if l2:
            while l2:
                if not l2:
                    return
                two.append(str(l2.val))
                l2 = l2.next
        
        one = str(int("".join(one)[::-1]) + int("".join(two)[::-1]))[::-1]
        one = [int(i) for i in one]
        if not one:
            return
        
        first = ListNode(one[0])
        final = first
        
        for _ in range(1, len(one)):
            node = ListNode(one[_])
            first.next = node
            first = node
            
        return final