class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        window = []
        stack = []
        
        
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
                
            stack.append(i)
            
            
            if stack[0] == i - k:
                stack.pop(0)
                
            if i >= k - 1:
                window.append(nums[stack[0]])
                
                
        return window