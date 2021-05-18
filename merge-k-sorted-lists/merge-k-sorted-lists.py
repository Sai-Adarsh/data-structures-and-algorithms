# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = []
        if not lists:
            return
        heapq.heapify(res)
        
        for head in lists:
            if not head:
                continue
            else:
                while head:
                    if not head:
                        break
                    heapq.heappush(res, head.val)
                    head = head.next
        
        res = [heapq.heappop(res) for _ in range(len(res))]
        if not res:
            return
        first = ListNode(res[0])
        final = first
        
        for _ in range(1, len(res)):
            node = ListNode(res[_])
            first.next = node
            first = node
            
        return final