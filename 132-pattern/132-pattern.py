class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        monotone_stack = []
        stack = []
        
        monotone_stack.append(nums[0])
        
        for i in range(1, len(nums)):
            monotone_stack.append(min(nums[:i]))
            
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > monotone_stack[i]:
                
                while stack and stack[-1] <= monotone_stack[i]:
                    stack.pop()
                    
                if stack and stack[-1] < nums[i]:
                    return True
                
                stack.append(nums[i])
                
        return False