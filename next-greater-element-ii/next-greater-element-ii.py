class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        output_arr = [0 for _ in range(len(nums))]
        stack = []
        
        for i in range(2 * len(nums)  -1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % len(nums)]:
                stack.pop()
            
            output_arr[i % len(nums)] = (-1 if not stack else nums[stack[-1]])
            stack.append(i % len(nums))
            
        return output_arr