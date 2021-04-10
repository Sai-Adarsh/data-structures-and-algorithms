class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        from collections import deque
        window = []
        stack = deque([])
        
        for i in range(len(nums)):
            
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            
            stack.append(i)
            
            if stack[0] == i - k:
                stack.popleft()
                
            if i >= k - 1:
                window.append(nums[stack[0]])
                
        return window