class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.nums = nums
        
        heapq.heapify(self.nums)
        
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
    def add(self, val: int) -> int:
        
        heap_top = 0
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val) 
        else:
            heapq.heappushpop(self.nums, val)
            
        return self.nums[heap_top]
                           
                           
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)