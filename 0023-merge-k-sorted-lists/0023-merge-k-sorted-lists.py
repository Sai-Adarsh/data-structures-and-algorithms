# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        heapq.heapify(res)
        for i in range(len(lists)):
            node = lists[i]
            while node:
                heapq.heappush(res, node.val)
                node = node.next
        retNode = None
        for _ in range(len(res)):
            if _ == 0:
                node = ListNode(heapq.heappop(res))
                retNode = node
            else:
                temp = ListNode(heapq.heappop(res))
                node.next = temp
                node = node.next
        return retNode