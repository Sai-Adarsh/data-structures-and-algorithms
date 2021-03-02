# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        root = ListNode(None)
        head = root
        for i in lists:
            while(i):
                root.next = i
                root = i
                i = i.next
        root = head.next
        L = []
        while(root):
            L.append(root.val)
            root = root.next
        L = sorted(L)
        
        node = ListNode(None)
        final = node
        for i in L:
            nn = ListNode(i)
            node.next = nn
            node = nn
        return final.next