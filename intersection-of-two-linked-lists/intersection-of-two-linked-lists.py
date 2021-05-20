# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        len_one = 0
        len_two = 0
        
        
        one = headA
        two = headB
        while one:
            if not one:
                return
            len_one += 1
            one = one.next
            
        
        while two:
            if not two:
                return
            len_two += 1
            two = two.next
            
        if len_two > len_one:
            for _ in range(len_two - len_one):
                headB = headB.next
        else:
            for _ in range(len_one - len_two):
                headA = headA.next
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            