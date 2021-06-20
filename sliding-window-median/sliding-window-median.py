class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        
        res = []
        range_stack = []
        
        for i in range(len(nums)):
            bisect.insort(range_stack, nums[i])
            
            if len(range_stack) >= k:
                if k % 2 == 0:
                    res.append((range_stack[len(range_stack) // 2] + range_stack[(len(range_stack) // 2) - 1]) / 2)
                else:
                    res.append(range_stack[len(range_stack) // 2])
                range_stack.remove(nums[i - k + 1])
                
        return res