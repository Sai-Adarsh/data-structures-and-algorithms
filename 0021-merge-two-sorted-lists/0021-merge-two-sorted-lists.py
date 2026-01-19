# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = []

        while list1:
            bisect.insort(temp, list1.val)
            list1 = list1.next
        
        while list2:
            bisect.insort(temp, list2.val)
            list2 = list2.next
        
        print(temp)
        
        newNode = None
        retNode = newNode
        if temp:
            newNode = ListNode(temp[0])
            retNode = newNode
        for i in range(1, len(temp)):
            tempNode = ListNode(temp[i])
            newNode.next = tempNode
            newNode = newNode.next


        return retNode
                