# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return
        
        nums = []
        
        while head:
            if not head:
                return
            nums.append(head.val)
            head = head.next
            
        
        res = [0 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res