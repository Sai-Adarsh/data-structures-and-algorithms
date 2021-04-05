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
            
        stack = []
        output_arr = [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                output_arr[stack.pop()] = nums[i]

            stack.append(i)
        
        return output_arr