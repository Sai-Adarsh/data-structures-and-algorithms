# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        if not head:
            return
        self.L = []
        while head:
            self.L.append(head.val)
            head = head.next
        G.sort()
        L = self.L
        for i in range(len(L)):
            if L[i] not in G:
                L[i] = '#'
            else:
                L[i] = str(L[i])
        res = []
        temp = ""
        for i in L:
            if i == '#':
                res.append(temp)
                temp = ""
            else:
                temp += i
        if temp != "":
            res.append(temp)
            temp = ""
        res = [i for i in res if '' * len(i) != i]
        return len(res)